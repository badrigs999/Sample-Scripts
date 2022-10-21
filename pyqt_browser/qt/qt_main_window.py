# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'X:\Software\staging\Bot_Browser\main_browser\ui\main_window.ui'
#
# Created: Fri Dec 11 16:59:53 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qtpy.QtGui import *
from qtpy.QtCore import *
from qtpy.QtWidgets import *

class Ui_MainWindow_Browser(object):
    def setupUi(self, MainWindow_Browser):
        MainWindow_Browser.setObjectName("MainWindow_Browser")
        MainWindow_Browser.resize(1036, 814)
        MainWindow_Browser.setAnimated(True)
        MainWindow_Browser.setTabShape(QTabWidget.Rounded)
        MainWindow_Browser.setDockNestingEnabled(False)
        MainWindow_Browser.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow_Browser.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow_Browser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow_Browser.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow_Browser)
        self.menubar.setGeometry(QRect(0, 0, 1036, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QMenu(self.menuFile)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow_Browser.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow_Browser)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Browser.setStatusBar(self.statusbar)
        self.actionNew = QAction(MainWindow_Browser)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QAction(MainWindow_Browser)
        self.actionClose.setObjectName("actionClose")
        self.actionHelp_2 = QAction(MainWindow_Browser)
        self.actionHelp_2.setObjectName("actionHelp_2")
        self.actionAbout_Window = QAction(MainWindow_Browser)
        self.actionAbout_Window.setObjectName("actionAbout_Window")
        self.actionUpdate = QAction(MainWindow_Browser)
        self.actionUpdate.setObjectName("actionUpdate")
        self.menuHelp.addAction(self.actionHelp_2)
        self.menuHelp.addAction(self.actionAbout_Window)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpdate)
        self.menuFile.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow_Browser)
        QMetaObject.connectSlotsByName(MainWindow_Browser)

    def retranslateUi(self, MainWindow_Browser):
        MainWindow_Browser.setWindowTitle(QApplication.translate("MainWindow_Browser", "Custom Explorer", None, QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QApplication.translate("MainWindow_Browser", "File", None, QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QApplication.translate("MainWindow_Browser", "Help", None, QApplication.UnicodeUTF8))
        self.actionNew.setText(QApplication.translate("MainWindow_Browser", "New Window", None, QApplication.UnicodeUTF8))
        self.actionClose.setText(QApplication.translate("MainWindow_Browser", "Close", None, QApplication.UnicodeUTF8))
        self.actionHelp_2.setText(QApplication.translate("MainWindow_Browser", "Help", None, QApplication.UnicodeUTF8))
        self.actionAbout_Window.setText(QApplication.translate("MainWindow_Browser", "About Window", None, QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QApplication.translate("MainWindow_Browser", "Update", None, QApplication.UnicodeUTF8))

