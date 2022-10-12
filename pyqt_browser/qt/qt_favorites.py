# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Desktop\layout.ui'
#
# Created: Mon Dec 14 17:04:15 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qtpy.QtGui import *
from qtpy.QtCore import *
from qtpy.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(425, 681)
        self.widget = QWidget(Form)
        self.widget.setGeometry(QRect(70, 80, 271, 444))
        self.widget.setObjectName("widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QSplitter(self.widget)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listWidget = QListWidget(self.widget1)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.widget2 = QWidget(self.splitter)
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget_2 = QListWidget(self.widget2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout.addWidget(self.listWidget_2)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("Form", "My Task:", None, QApplication.UnicodeUTF8))
        self.label_2.setText(QApplication.translate("Form", "Quick Access:", None, QApplication.UnicodeUTF8))