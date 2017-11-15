# coding=utf-8

"""Definitions about InaSAFE reports."""

from safe.utilities.i18n import tr

__copyright__ = "Copyright 2016, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'

"""General descriptions of the different reports produced by InaSAFE."""

infographic_report_description = {
  'name': tr('Infographic report'),
  'customisable': True,
  'description': tr(
    'Only generated for cases where the exposure dataset is population, '
    'the infographic report provides a visual "at a glance" overview '
    'of the impacts population. It uses the Indonesian minimum needs '
    'profile, so users in other countries should probably implement '
    'a customised version of this report which caters for their local '
    'minimum needs profile.'),
  # place thumbs in resources/img/screenshots for them to appear in help
  'thumbnail': 'infographic-thumbnail-screenshot.png'
}
impact_report_description = {
  'name': tr('Impact report'),
  'customisable': False,
  'description': tr(
    'The impact report provides a tabular overview of the analysis including '
    'details of the analysis question, the general report, the minimum '
    'needs and other demographic breakdowns (when exposure is population), a '
    'list of notes and assumptions and basic details of the datasets used '
    'in the analysis.'),
  # place thumbs in resources/img/screenshots for them to appear in help
  'thumbnail': 'impact-report-thumbnail-screenshot.png'
}
portrait_map_report_description = {
  'name': tr('Portrait map'),
  'orientation': 'portrait',
  'customisable': True,
  'description': tr(
    'A standard map report is produced in a portrait layout '
    'for this report. We provide both portrait and landscape layouts so '
    'that the reports can accommodate different shapes of reporting area. '
    'The master template for this report is found in the InaSAFE plugin '
    'directory under "resources/qgis-composer-templates/inasafe-map-report'
    '-portrait.qpt". If you make a copy of this report to your "<home>/'
    '.qgis2/inasafe" directory, you can edit this copy and override the '
    'default layout and content options provided by InaSAFE. See also '
    'the manual for details about expressions and composer elements that '
    'you can use in your reports. In addition to this basic override '
    'mechanism, you can provide hazard / exposure specific variants of '
    'this template by using the following path and naming convention: '
    '"(home)/.qgis2/inasafe/inasafe-map-report-portrait-'
    '(hazard)-(exposure).qpt" (where (home) is replaced by the path to '
    'your home directory, (hazard) by the class of hazard, and (exposure) '
    'by the class of exposure).'),
  # place thumbs in resources/img/screenshots for them to appear in help
  'thumbnail': 'portrait-map-report-thumbnail.png'
}
landscape_map_report_description = {
  'name': tr('Landscape map'),
  'orientation': 'landscape',
  'customisable': True,
  'description': tr(
    'A standard map report is produced in a landscape layout. '
    'We provide both portrait and landscape layouts so '
    'that the reports can accommodate different shapes of reporting area. '
    'The master template for this report is found in the InaSAFE plugin '
    'directory under "resources/qgis-composer-templates/inasafe-map-report'
    '-landscape.qpt". If you make a copy of this report to your "<home>/'
    '.qgis2/inasafe" directory, you can edit this copy and override the '
    'default layout and content options provided by InaSAFE. See also '
    'the manual for details about expressions and composer elements that '
    'you can use in your reports. In addition to this basic override '
    'mechanism, you can provide hazard / exposure specific variants of '
    'this template by using the following path and naming convention: '
    '"(home)/.qgis2/inasafe/inasafe-map-report-landscape-'
    '(hazard)-(exposure).qpt" (where (home) is replaced by the path to '
    'your home directory, (hazard) by the class of hazard, and (exposure) '
    'by the class of exposure).'),
  # place thumbs in resources/img/screenshots for them to appear in help
  'thumbnail': 'lanscape-map-report-thumbnail.png'
}
analysis_provenance_report_description = {
  'name': tr('Analysis provenance'),
  'customisable': False,
  'description': tr(
    'When providing a report generated by InaSAFE to a decision make, '
    'it is important that there is accompanying information that '
    'describes which datasets were used, what settings were used, and so on. '
    'The provenance report is designed to address this need by providing '
    'detailed technical information about the analysis.'),
  # place thumbs in resources/img/screenshots for them to appear in help
  'thumbnail': 'provenance-report-thumbnail.png'
}
action_checklist_report_description = {
  'name': tr('Action checklist'),
  'customisable': False,
  'description': tr(
    'The action checklist report provides a list of actions for the '
    'DRR practitioner to be aware of or think about. These include '
    'general items such as "how will warnings be disseminated?" and '
    'specific items such as things that relate to displaced '
    'people if the exposure of the analysis is population.'),
  # place thumbs in resources/img/screenshots for them to appear in help
  'thumbnail': 'action-checklist-report.png'
}

all_reports = [
    infographic_report_description,
    impact_report_description,
    portrait_map_report_description,
    landscape_map_report_description,
    action_checklist_report_description,
    analysis_provenance_report_description,
]
