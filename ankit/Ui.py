# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sip
sip.setapi('QString', 1)
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(529, 318)
        Dialog.setAutoFillBackground(True)
        Dialog.setModal(False)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.l10 = QtGui.QLabel(Dialog)
        self.l10.setStyleSheet(_fromUtf8("border-color: rgb(104, 34, 255);\n"
"border: 2px solid;\n"
"color: blue;"))
        self.l10.setObjectName(_fromUtf8("l10"))
        self.gridLayout.addWidget(self.l10, 4, 0, 1, 1)
        self.v11 = QtGui.QLabel(Dialog)
        self.v11.setObjectName(_fromUtf8("v11"))
        self.gridLayout.addWidget(self.v11, 4, 3, 1, 1)
        self.l01 = QtGui.QLabel(Dialog)
        self.l01.setStyleSheet(_fromUtf8("border: 2px solid black;\n"
"color:blue;"))
        self.l01.setObjectName(_fromUtf8("l01"))
        self.gridLayout.addWidget(self.l01, 2, 2, 1, 1)
        self.v01 = QtGui.QLabel(Dialog)
        self.v01.setObjectName(_fromUtf8("v01"))
        self.gridLayout.addWidget(self.v01, 2, 3, 1, 1)
        self.l00 = QtGui.QLabel(Dialog)
        self.l00.setStyleSheet(_fromUtf8("border-color: rgb(104, 34, 255);\n"
"border: 2px solid;\n"
"color: blue;"))
        self.l00.setObjectName(_fromUtf8("l00"))
        self.gridLayout.addWidget(self.l00, 2, 0, 1, 1)
        self.closeButton = QtGui.QPushButton(Dialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 6, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.v10 = QtGui.QLabel(Dialog)
        self.v10.setObjectName(_fromUtf8("v10"))
        self.gridLayout.addWidget(self.v10, 4, 1, 1, 1)
        self.v00 = QtGui.QLabel(Dialog)
        self.v00.setObjectName(_fromUtf8("v00"))
        self.gridLayout.addWidget(self.v00, 2, 1, 1, 1)
        self.l11 = QtGui.QLabel(Dialog)
        self.l11.setStyleSheet(_fromUtf8("border: 2px solid black;\n"
"color:blue;"))
        self.l11.setObjectName(_fromUtf8("l11"))
        self.gridLayout.addWidget(self.l11, 4, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.heading = QtGui.QLabel(Dialog)
        self.heading.setObjectName(_fromUtf8("heading"))
        self.gridLayout.addWidget(self.heading, 1, 0, 1, 4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.l10.setText(_translate("Dialog", "Temperature of the node", None))
        self.v11.setText(_translate("Dialog", "TextLabel", None))
        self.l01.setText(_translate("Dialog", "Battery of the node", None))
        self.v01.setText(_translate("Dialog", "TextLabel", None))
        self.l00.setText(_translate("Dialog", "Temperature of the node", None))
        self.closeButton.setText(_translate("Dialog", "Close", None))
        self.v10.setText(_translate("Dialog", "TextLabel", None))
        self.v00.setText(_translate("Dialog", "TextLabel", None))
        self.l11.setText(_translate("Dialog", "Battery of the node", None))
        self.heading.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic;\">RPI Motor monitor</span></p></body></html>", None))

