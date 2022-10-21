# -*- coding: utf-8 -*-

# default
import os
import sys

realpath = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(realpath, "qt"))
sys.path.insert(0, os.path.join(realpath, "support_files"))

# custom
from qt_element_browser import Ui_Form


# pip
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
import qdarkstyle


class ElementBrowser(Ui_Form, QWidget):

    def __init__(self, parent=None):
        super(ElementBrowser, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Element Browser")

        self.preview_state = "grid"
        self.icon_path = os.path.join(realpath, "images")

        self.set_preset_icon()
        self.preview_settings()
        self.signal_slots_actions()

    def signal_slots_actions(self):
        self.tb_ele_add.clicked.connect(self.add_element)
        self.tb_ele_remove.clicked.connect(self.remove_element)
        self.tb_view.clicked.connect(self.preview_settings)

    def add_element(self):
        print ("add element")

    def remove_element(self):
        print ("remove element")

    def preview_settings(self):
        if self.preview_state == "grid":
            self.tb_view.setIcon(QIcon(os.path.join(self.icon_path, "grid.png")))
            self.preview_state = "item"
            self.tw_item_preview.hide()
            self.lw_img_preview.show()
        else:
            self.tb_view.setIcon(QIcon(os.path.join(self.icon_path, "item.png")))
            self.preview_state = "grid"
            self.tw_item_preview.show()
            self.lw_img_preview.hide()

    def set_preset_icon(self):
        self.setWindowIcon(QIcon(os.path.join(self.icon_path, "element.png")))
        self.tb_home.setIcon(QIcon(os.path.join(self.icon_path, "home.png")))
        self.tb_ingest.setIcon(QIcon(os.path.join(self.icon_path, "ingest.png")))
        self.tb_settings.setIcon(QIcon(os.path.join(self.icon_path, "settings.png")))
        self.tb_view.setIcon(QIcon(os.path.join(self.icon_path, "grid.png")))
        self.tb_refresh.setIcon(QIcon(os.path.join(self.icon_path, "refresh.png")))
        self.tb_fav.setIcon(QIcon(os.path.join(self.icon_path, "fav.png")))
        self.tb_ele_add.setIcon(QIcon(os.path.join(self.icon_path, "add.png")))
        self.tb_ele_remove.setIcon(QIcon(os.path.join(self.icon_path, "remove.png")))

def main():
    app = QApplication([])
    widget = ElementBrowser()
    widget.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()