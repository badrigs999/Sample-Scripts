# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'X:\Software\staging\Bot_Browser\main_browser\ui\main_window.ui'
#
# Created: Fri Dec 11 16:59:53 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow_Browser(object):
    def setupUi(self, MainWindow_Browser):
        MainWindow_Browser.setObjectName("MainWindow_Browser")
        MainWindow_Browser.resize(1036, 814)
        MainWindow_Browser.setAnimated(True)
        MainWindow_Browser.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow_Browser.setDockNestingEnabled(False)
        MainWindow_Browser.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow_Browser.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow_Browser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow_Browser.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow_Browser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menuFile)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow_Browser.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow_Browser)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Browser.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow_Browser)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtGui.QAction(MainWindow_Browser)
        self.actionClose.setObjectName("actionClose")
        self.actionHelp_2 = QtGui.QAction(MainWindow_Browser)
        self.actionHelp_2.setObjectName("actionHelp_2")
        self.actionAbout_Window = QtGui.QAction(MainWindow_Browser)
        self.actionAbout_Window.setObjectName("actionAbout_Window")
        self.actionUpdate = QtGui.QAction(MainWindow_Browser)
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Browser)

    def retranslateUi(self, MainWindow_Browser):
        MainWindow_Browser.setWindowTitle(QtGui.QApplication.translate("MainWindow_Browser", "Custom Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow_Browser", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow_Browser", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow_Browser", "New Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow_Browser", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp_2.setText(QtGui.QApplication.translate("MainWindow_Browser", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Window.setText(QtGui.QApplication.translate("MainWindow_Browser", "About Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("MainWindow_Browser", "Update", None, QtGui.QApplication.UnicodeUTF8))

