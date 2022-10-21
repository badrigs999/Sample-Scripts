# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_browser.ui'
#
# Created: Mon Dec 14 19:07:25 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qtpy.QtGui import *
from qtpy.QtCore import *
from qtpy.QtWidgets import *

class Ui_botBrowserTabWidget_2(object):
    def setupUi(self, botBrowserTabWidget_2):
        botBrowserTabWidget_2.setObjectName("botBrowserTabWidget_2")
        botBrowserTabWidget_2.resize(990, 768)
        self.gridLayout = QGridLayout(botBrowserTabWidget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.botBrowserTabWidget = QTabWidget(botBrowserTabWidget_2)
        self.botBrowserTabWidget.setObjectName("botBrowserTabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter_2 = QSplitter(self.tab)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QWidget(self.splitter_2)
        self.widget.setMinimumSize(QSize(220, 16777215))
        self.widget.setMaximumSize(QSize(220, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QSplitter(self.widget)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listWidget = QListWidget(self.layoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget_2 = QListWidget(self.layoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout.addWidget(self.listWidget_2)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        # self.explorer_widget = QWidget(self.splitter_2)
        # self.explorer_widget.setObjectName("explorer_widget")
        self.gridLayout_4.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.botBrowserTabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.adv_explorer_widget = QWidget(self.tab_2)
        self.adv_explorer_widget.setObjectName("adv_explorer_widget")
        self.gridLayout_3.addWidget(self.adv_explorer_widget, 0, 0, 1, 1)
        self.botBrowserTabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.botBrowserTabWidget, 0, 0, 1, 1)

        self.retranslateUi(botBrowserTabWidget_2)
        self.botBrowserTabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(botBrowserTabWidget_2)

    def retranslateUi(self, botBrowserTabWidget_2):
        botBrowserTabWidget_2.setWindowTitle(QApplication.translate("botBrowserTabWidget_2", "Form", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("botBrowserTabWidget_2", "My Task:", None, QApplication.UnicodeUTF8))
        self.label_2.setText(QApplication.translate("botBrowserTabWidget_2", "Quick Access:", None, QApplication.UnicodeUTF8))
        self.botBrowserTabWidget.setTabText(self.botBrowserTabWidget.indexOf(self.tab), QApplication.translate("botBrowserTabWidget_2", "Explorer", None, QApplication.UnicodeUTF8))
        self.botBrowserTabWidget.setTabText(self.botBrowserTabWidget.indexOf(self.tab_2), QApplication.translate("botBrowserTabWidget_2", "Show View", None, QApplication.UnicodeUTF8))

