# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keywords_dialog_base.ui'
#
# Created: Fri Jun  7 09:18:55 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_KeywordsDialogBase(object):
    def setupUi(self, KeywordsDialogBase):
        KeywordsDialogBase.setObjectName(_fromUtf8("KeywordsDialogBase"))
        KeywordsDialogBase.resize(515, 667)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(KeywordsDialogBase.sizePolicy().hasHeightForWidth())
        KeywordsDialogBase.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KeywordsDialogBase.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(KeywordsDialogBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblLayerName = QtGui.QLabel(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLayerName.sizePolicy().hasHeightForWidth())
        self.lblLayerName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLayerName.setFont(font)
        self.lblLayerName.setText(_fromUtf8(""))
        self.lblLayerName.setWordWrap(True)
        self.lblLayerName.setObjectName(_fromUtf8("lblLayerName"))
        self.verticalLayout.addWidget(self.lblLayerName)
        self.grpSimple = QtGui.QGroupBox(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpSimple.sizePolicy().hasHeightForWidth())
        self.grpSimple.setSizePolicy(sizePolicy)
        self.grpSimple.setObjectName(_fromUtf8("grpSimple"))
        self.gridLayout_3 = QtGui.QGridLayout(self.grpSimple)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.cboFemaleRatioAttribute = QtGui.QComboBox(self.grpSimple)
        self.cboFemaleRatioAttribute.setObjectName(_fromUtf8("cboFemaleRatioAttribute"))
        self.gridLayout_3.addWidget(self.cboFemaleRatioAttribute, 4, 1, 1, 1)
        self.cboSubcategory = QtGui.QComboBox(self.grpSimple)
        self.cboSubcategory.setObjectName(_fromUtf8("cboSubcategory"))
        self.gridLayout_3.addWidget(self.cboSubcategory, 2, 1, 1, 1)
        self.lblSubcategory = QtGui.QLabel(self.grpSimple)
        self.lblSubcategory.setObjectName(_fromUtf8("lblSubcategory"))
        self.gridLayout_3.addWidget(self.lblSubcategory, 2, 0, 1, 1)
        self.cboAggregationAttribute = QtGui.QComboBox(self.grpSimple)
        self.cboAggregationAttribute.setObjectName(_fromUtf8("cboAggregationAttribute"))
        self.gridLayout_3.addWidget(self.cboAggregationAttribute, 3, 1, 1, 1)
        self.lblAggregationAttribute = QtGui.QLabel(self.grpSimple)
        self.lblAggregationAttribute.setEnabled(True)
        self.lblAggregationAttribute.setObjectName(_fromUtf8("lblAggregationAttribute"))
        self.gridLayout_3.addWidget(self.lblAggregationAttribute, 3, 0, 1, 1)
        self.lblCategory = QtGui.QLabel(self.grpSimple)
        self.lblCategory.setObjectName(_fromUtf8("lblCategory"))
        self.gridLayout_3.addWidget(self.lblCategory, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radHazard = QtGui.QRadioButton(self.grpSimple)
        self.radHazard.setObjectName(_fromUtf8("radHazard"))
        self.horizontalLayout_3.addWidget(self.radHazard)
        self.radExposure = QtGui.QRadioButton(self.grpSimple)
        self.radExposure.setChecked(True)
        self.radExposure.setObjectName(_fromUtf8("radExposure"))
        self.horizontalLayout_3.addWidget(self.radExposure)
        self.radPostprocessing = QtGui.QRadioButton(self.grpSimple)
        self.radPostprocessing.setObjectName(_fromUtf8("radPostprocessing"))
        self.horizontalLayout_3.addWidget(self.radPostprocessing)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.leTitle = QtGui.QLineEdit(self.grpSimple)
        self.leTitle.setObjectName(_fromUtf8("leTitle"))
        self.gridLayout_3.addWidget(self.leTitle, 0, 1, 1, 1)
        self.lblTitle = QtGui.QLabel(self.grpSimple)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.gridLayout_3.addWidget(self.lblTitle, 0, 0, 1, 1)
        self.lblFemaleRatioAttribute = QtGui.QLabel(self.grpSimple)
        self.lblFemaleRatioAttribute.setObjectName(_fromUtf8("lblFemaleRatioAttribute"))
        self.gridLayout_3.addWidget(self.lblFemaleRatioAttribute, 4, 0, 1, 1)
        self.lblFemaleRatioDefault = QtGui.QLabel(self.grpSimple)
        self.lblFemaleRatioDefault.setObjectName(_fromUtf8("lblFemaleRatioDefault"))
        self.gridLayout_3.addWidget(self.lblFemaleRatioDefault, 5, 0, 1, 1)
        self.dsbFemaleRatioDefault = QtGui.QDoubleSpinBox(self.grpSimple)
        self.dsbFemaleRatioDefault.setAccelerated(True)
        self.dsbFemaleRatioDefault.setMaximum(1.0)
        self.dsbFemaleRatioDefault.setSingleStep(0.01)
        self.dsbFemaleRatioDefault.setProperty("value", 0.0)
        self.dsbFemaleRatioDefault.setObjectName(_fromUtf8("dsbFemaleRatioDefault"))
        self.gridLayout_3.addWidget(self.dsbFemaleRatioDefault, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.grpSimple)
        self.pbnAdvanced = QtGui.QPushButton(KeywordsDialogBase)
        self.pbnAdvanced.setCheckable(True)
        self.pbnAdvanced.setObjectName(_fromUtf8("pbnAdvanced"))
        self.verticalLayout.addWidget(self.pbnAdvanced)
        self.grpAdvanced = QtGui.QGroupBox(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpAdvanced.sizePolicy().hasHeightForWidth())
        self.grpAdvanced.setSizePolicy(sizePolicy)
        self.grpAdvanced.setObjectName(_fromUtf8("grpAdvanced"))
        self.gridLayout = QtGui.QGridLayout(self.grpAdvanced)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radPredefined = QtGui.QRadioButton(self.grpAdvanced)
        self.radPredefined.setObjectName(_fromUtf8("radPredefined"))
        self.horizontalLayout_4.addWidget(self.radPredefined)
        self.radUserDefined = QtGui.QRadioButton(self.grpAdvanced)
        self.radUserDefined.setObjectName(_fromUtf8("radUserDefined"))
        self.horizontalLayout_4.addWidget(self.radUserDefined)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.framePredefined = QtGui.QFrame(self.grpAdvanced)
        self.framePredefined.setFrameShape(QtGui.QFrame.StyledPanel)
        self.framePredefined.setFrameShadow(QtGui.QFrame.Raised)
        self.framePredefined.setObjectName(_fromUtf8("framePredefined"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.framePredefined)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.framePredefined)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.cboKeyword = QtGui.QComboBox(self.framePredefined)
        self.cboKeyword.setObjectName(_fromUtf8("cboKeyword"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(0, _fromUtf8("subcategory"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(1, _fromUtf8("unit"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(2, _fromUtf8("datatype"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cboKeyword)
        self.label_5 = QtGui.QLabel(self.framePredefined)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lePredefinedValue = QtGui.QLineEdit(self.framePredefined)
        self.lePredefinedValue.setObjectName(_fromUtf8("lePredefinedValue"))
        self.horizontalLayout.addWidget(self.lePredefinedValue)
        self.pbnAddToList1 = QtGui.QPushButton(self.framePredefined)
        self.pbnAddToList1.setObjectName(_fromUtf8("pbnAddToList1"))
        self.horizontalLayout.addWidget(self.pbnAddToList1)
        self.gridLayout.addWidget(self.framePredefined, 1, 0, 1, 1)
        self.frameUserDefined = QtGui.QFrame(self.grpAdvanced)
        self.frameUserDefined.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameUserDefined.setFrameShadow(QtGui.QFrame.Raised)
        self.frameUserDefined.setObjectName(_fromUtf8("frameUserDefined"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frameUserDefined)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.frameUserDefined)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.leKey = QtGui.QLineEdit(self.frameUserDefined)
        self.leKey.setObjectName(_fromUtf8("leKey"))
        self.horizontalLayout_2.addWidget(self.leKey)
        self.label_7 = QtGui.QLabel(self.frameUserDefined)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.leValue = QtGui.QLineEdit(self.frameUserDefined)
        self.leValue.setObjectName(_fromUtf8("leValue"))
        self.horizontalLayout_2.addWidget(self.leValue)
        self.pbnAddToList2 = QtGui.QPushButton(self.frameUserDefined)
        self.pbnAddToList2.setObjectName(_fromUtf8("pbnAddToList2"))
        self.horizontalLayout_2.addWidget(self.pbnAddToList2)
        self.gridLayout.addWidget(self.frameUserDefined, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.grpAdvanced)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lstKeywords = QtGui.QListWidget(self.grpAdvanced)
        self.lstKeywords.setAlternatingRowColors(True)
        self.lstKeywords.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.lstKeywords.setObjectName(_fromUtf8("lstKeywords"))
        self.gridLayout.addWidget(self.lstKeywords, 4, 0, 1, 1)
        self.lblMessage = QtGui.QLabel(self.grpAdvanced)
        self.lblMessage.setStyleSheet(_fromUtf8("color: red;"))
        self.lblMessage.setText(_fromUtf8(""))
        self.lblMessage.setTextFormat(QtCore.Qt.RichText)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.gridLayout.addWidget(self.lblMessage, 5, 0, 1, 1)
        self.pbnRemove = QtGui.QPushButton(self.grpAdvanced)
        self.pbnRemove.setObjectName(_fromUtf8("pbnRemove"))
        self.gridLayout.addWidget(self.pbnRemove, 6, 0, 1, 1)
        self.verticalLayout.addWidget(self.grpAdvanced)
        self.buttonBox = QtGui.QDialogButtonBox(KeywordsDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.lblSubcategory.setBuddy(self.cboSubcategory)
        self.label_4.setBuddy(self.cboKeyword)
        self.label_6.setBuddy(self.leKey)
        self.label_7.setBuddy(self.leValue)
        self.label_8.setBuddy(self.lstKeywords)

        self.retranslateUi(KeywordsDialogBase)
        QtCore.QObject.connect(self.radPredefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frameUserDefined.setHidden)
        QtCore.QObject.connect(self.radUserDefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.framePredefined.setHidden)
        QtCore.QObject.connect(self.radPredefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.framePredefined.setVisible)
        QtCore.QObject.connect(self.radUserDefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frameUserDefined.setVisible)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), KeywordsDialogBase.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), KeywordsDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(KeywordsDialogBase)
        KeywordsDialogBase.setTabOrder(self.radHazard, self.pbnAdvanced)
        KeywordsDialogBase.setTabOrder(self.pbnAdvanced, self.radPredefined)
        KeywordsDialogBase.setTabOrder(self.radPredefined, self.cboKeyword)
        KeywordsDialogBase.setTabOrder(self.cboKeyword, self.pbnAddToList1)
        KeywordsDialogBase.setTabOrder(self.pbnAddToList1, self.leKey)
        KeywordsDialogBase.setTabOrder(self.leKey, self.leValue)
        KeywordsDialogBase.setTabOrder(self.leValue, self.pbnAddToList2)
        KeywordsDialogBase.setTabOrder(self.pbnAddToList2, self.lstKeywords)
        KeywordsDialogBase.setTabOrder(self.lstKeywords, self.pbnRemove)
        KeywordsDialogBase.setTabOrder(self.pbnRemove, self.buttonBox)

    def retranslateUi(self, KeywordsDialogBase):
        KeywordsDialogBase.setWindowTitle(_translate("KeywordsDialogBase", "InaSAFE - Keyword Editor", None))
        self.grpSimple.setTitle(_translate("KeywordsDialogBase", "Quick edit", None))
        self.cboSubcategory.setToolTip(_translate("KeywordsDialogBase", "A subcategory represents the type of hazard.", None))
        self.lblSubcategory.setText(_translate("KeywordsDialogBase", "Subcategory", None))
        self.lblAggregationAttribute.setText(_translate("KeywordsDialogBase", "Aggregation attribute", None))
        self.lblCategory.setText(_translate("KeywordsDialogBase", "Category", None))
        self.radHazard.setToolTip(_translate("KeywordsDialogBase", "A hazard is a situation that poses a level of threat to life, health, property, or environment. (Wikipedia)", None))
        self.radHazard.setText(_translate("KeywordsDialogBase", "Hazard", None))
        self.radExposure.setToolTip(_translate("KeywordsDialogBase", "Where people and property are situated.", None))
        self.radExposure.setText(_translate("KeywordsDialogBase", "Exposure", None))
        self.radPostprocessing.setText(_translate("KeywordsDialogBase", "Postprocessing", None))
        self.lblTitle.setText(_translate("KeywordsDialogBase", "Title", None))
        self.lblFemaleRatioAttribute.setText(_translate("KeywordsDialogBase", "Female ratio attribute", None))
        self.lblFemaleRatioDefault.setText(_translate("KeywordsDialogBase", "Female ratio default", None))
        self.pbnAdvanced.setText(_translate("KeywordsDialogBase", "Show advanced editor", None))
        self.grpAdvanced.setTitle(_translate("KeywordsDialogBase", "Advanced editor", None))
        self.radPredefined.setText(_translate("KeywordsDialogBase", "Predefined", None))
        self.radUserDefined.setText(_translate("KeywordsDialogBase", "User defined", None))
        self.label_4.setText(_translate("KeywordsDialogBase", "Keyword", None))
        self.cboKeyword.setItemText(3, _translate("KeywordsDialogBase", "source", None))
        self.label_5.setText(_translate("KeywordsDialogBase", "Value", None))
        self.pbnAddToList1.setText(_translate("KeywordsDialogBase", "Add to list", None))
        self.label_6.setText(_translate("KeywordsDialogBase", "Key", None))
        self.label_7.setText(_translate("KeywordsDialogBase", "Value", None))
        self.pbnAddToList2.setText(_translate("KeywordsDialogBase", "Add to list", None))
        self.label_8.setText(_translate("KeywordsDialogBase", "Current keywords", None))
        self.pbnRemove.setText(_translate("KeywordsDialogBase", "Remove selected", None))

import resources_rc
