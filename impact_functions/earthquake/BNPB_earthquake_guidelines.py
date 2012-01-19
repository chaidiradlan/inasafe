"""Impact function based on Padang 2009 post earthquake survey

This impact function estimates percentual damage to buildings as a
function of ground shaking measured in MMI.
Buildings are currently assumed to be represented in OpenStreetMap with
attributes collected as during the July 2011 Indonesian mapping competition.

This impact function maps the OSM buildings into 2 classes:
Unreinforced masonry (URM) and reinforced masonry (RM) according to
the guidelines.
"""

from impact_functions.core import FunctionProvider
from impact_functions.core import get_hazard_layer, get_exposure_layer
from storage.vector import Vector
from storage.utilities import ugettext as _
from impact_functions.utilities import PointZoomSize
from impact_functions.utilities import PointClassColor
from impact_functions.utilities import PointSymbol
from impact_functions.mappings import osm2bnpb, unspecific2bnpb, sigab2bnpb

# Damage 'curves' for the two vulnerability classes
damage_parameters = {'URM': [6, 7],
                     'RM': [6, 8]}


class EarthquakeGuidelinesFunction(FunctionProvider):
    """Risk plugin for BNPB guidelines for earthquake damage to buildings

    :param requires category=='hazard' and \
                    subcategory.startswith('earthquake') and \
                    layer_type=='raster' and \
                    unit=='MMI'

    :param requires category=='exposure' and \
                    subcategory.startswith('building') and \
                    layer_type=='vector'
    """

    vclass_tag = 'VCLASS'
    target_field = 'DMGLEVEL'

    def run(self, layers):
        """Risk plugin for earthquake school damage
        """

        # Extract data
        H = get_hazard_layer(layers)    # Ground shaking
        E = get_exposure_layer(layers)  # Building locations

        keywords = E.get_keywords()
        if 'datatype' in keywords:
            datatype = keywords['datatype']
            if datatype.lower() == 'osm':
                # Map from OSM attributes to the guideline classes (URM and RM)
                E = osm2bnpb(E, target_attribute=self.vclass_tag)
            elif datatype.lower() == 'sigab':
                # Map from SIGAB attributes to the guideline classes
                # (URM and RM)
                E = sigab2bnpb(E)
            else:
                E = unspecific2bnpb(E, target_attribute=self.vclass_tag)
        else:
            E = unspecific2bnpb(E, target_attribute=self.vclass_tag)

        # Interpolate hazard level to building locations
        H = H.interpolate(E)

        # Extract relevant numerical data
        coordinates = E.get_geometry()
        shaking = H.get_data()
        N = len(shaking)

        # List attributes to carry forward to result layer
        attributes = E.get_attribute_names()

        # Calculate building damage
        count3 = 0
        count2 = 0
        count1 = 0
        building_damage = []
        for i in range(N):
            mmi = float(shaking[i].values()[0])

            building_class = E.get_data(self.vclass_tag, i)
            lo, hi = damage_parameters[building_class]

            if mmi < lo:
                damage = 1  # Low
                count1 += 1
            elif lo <= mmi < hi:
                damage = 2  # Medium
                count2 += 1
            else:
                damage = 3  # High
                count3 += 1

            # Collect shake level and calculated damage
            result_dict = {self.target_field: damage,
                           'MMI': mmi}

            # Carry all orginal attributes forward
            for key in attributes:
                result_dict[key] = E.get_data(key, i)

            # Record result for this feature
            building_damage.append(result_dict)

        # Create report
        caption = ('<table border="0" width="320px">'
                   '   <tr><th><b>%s</b></th><th><b>%s</b></th></th>'
                    '   <tr></tr>'
                    '   <tr><td>%s&#58;</td><td>%i</td></tr>'
                    '   <tr><td>%s (10-25%%)&#58;</td><td>%i</td></tr>'
                    '   <tr><td>%s (25-50%%)&#58;</td><td>%i</td></tr>'
                    '   <tr><td>%s (50-100%%)&#58;</td><td>%i</td></tr>'
                    '</table>' % (_('Buildings'), _('Total'),
                                  _('All'), N,
                                  _('Low damage'), count1,
                                  _('Medium damage'), count2,
                                  _('High damage'), count3))

        # Create style
        style_classes = [dict(label=_('Low damage'), min=0.5, max=1.5,
                              colour='#fecc5c', opacity=1),
                         dict(label=_('Medium damage'), min=1.5, max=2.5,
                              colour='#fd8d3c', opacity=1),
                         dict(label=_('High damage'), min=2.5, max=3.5,
                              colour='#f31a1c', opacity=1)]
        style_info = dict(target_field=self.target_field,
                          style_classes=style_classes)

        # Create vector layer and return
        V = Vector(data=building_damage,
                   projection=E.get_projection(),
                   geometry=coordinates,
                   name='Estimated damage level',
                   keywords={'caption': caption},
                   style_info=style_info)

        return V
