# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(dir_path, "qt"))
sys.path.insert(0, os.path.join(dir_path, "explorer_window"))

from main import Project_Browser_Widget
import utilities
import gui_utilities

from qt_main_window import Ui_MainWindow_Browser
from qt_tab_browser import Ui_botBrowserTabWidget_2

class CustomBrowser(QMainWindow, Ui_MainWindow_Browser):
    """docstring for CustomBrowser"""
    def __init__(self, parent=None):
        super(CustomBrowser, self).__init__(parent)
        self.setupUi(self)

        self.tab_browser = Custom_Browser_Tab_Widget()

        # Hide Main window statusBar
        self.statusBar().hide()

        # add Tab Browser
        self.gridLayout.addWidget(self.tab_browser, 0, 0, 1, 1)

class Custom_Browser_Tab_Widget(QWidget, Ui_botBrowserTabWidget_2):
    """docstring for Custom_Browser_Tab_Widget"""
    def __init__(self, parent=None):
        super(Custom_Browser_Tab_Widget, self).__init__(parent)
        self.setupUi(self)
        
        self.project_browser = Project_Browser_Widget()
        # print (self.project_browser, type(self.project_browser))
        self.gridLayout_4.addWidget(self.project_browser, 0, 1, 1, 1)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    gui_utilities.register_resources()
    gui_utilities.set_theme()
    icon_path = os.path.join(utilities.find_image_dir(),'project_browser.png')
    app.setWindowIcon(QIcon(icon_path))
    
    main_widget = CustomBrowser()
    main_widget.setWindowTitle("Custom Browser")
    
    main_widget.show()
    main_widget.raise_()
    sys.exit(app.exec_())
