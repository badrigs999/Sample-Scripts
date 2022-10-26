# -*- coding: utf-8 -*-

# default
import os
import sys

# custom env
realpath = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(realpath, "qt"))
sys.path.insert(0, os.path.join(realpath, "support_files"))

# custom
from qt_element_browser import Ui_Form
import element_item

# pip
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
import qdarkstyle


class ElementBrowser(Ui_Form, QWidget):
    """
    Element browser is library for the asset or reuseable data files.
    """

    def __init__(self, parent=None):
        super(ElementBrowser, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Element Browser")

        self.preview_state = "grid"
        self.icon_path = os.path.join(realpath, "images")

        self.set_preset_icon()
        self.preview_settings()
        self.signal_slots_actions()
        self.widget_settings()

    def signal_slots_actions(self):
        self.tb_ele_add.clicked.connect(self.view_element)
        self.tb_ele_remove.clicked.connect(self.remove_element)
        self.tb_view.clicked.connect(self.preview_settings)
        self.hslider_grid.valueChanged.connect(self.change_image_size)

    def widget_settings(self):
        self.hslider_grid.setValue(50)
        self.lw_img_preview.setViewMode(QListView.IconMode)
        self.lw_img_preview.setFlow(QListView.LeftToRight)
        self.lw_img_preview.setGridSize(QSize(element_item.width+10, element_item.height+10))
        self.lw_img_preview.setResizeMode(QListView.Adjust)

    def change_image_size(self, value):
        print ("Value: ", value)
        for i in range(self.lw_img_preview.count()):
            item = self.lw_img_preview.item(i)
            a = item.listWidget()
            cur_width = element_item.width+int(value)
            cur_height = element_item.height-25+int(value)
            self.lw_img_preview.setGridSize(QSize(cur_width, cur_height))
            self.thumbRect = QRect(0, 0, width, height-25)
            print (a)

    def add_element(self):
        print ("add element")

    def remove_element(self):
        print ("remove element")

    def view_element(self):

        for each in range(10):
            # For Grid View
            grid_widget = element_item.ScrollingThumbnail(self.lw_img_preview, QPixmap(r"D:\storage\video_preview.jpg"))
            item =  QListWidgetItem("images")
            self.lw_img_preview.insertItem(self.lw_img_preview.count(), item)
            self.lw_img_preview.setItemWidget(item, grid_widget)
            item.setSizeHint(QSize(element_item.width, element_item.height))
            item.setTextAlignment(Qt.AlignBottom)

            # For Item View
            item_widget = element_item.ScrollingThumbnail(self.tw_item_preview, QPixmap(r"D:\storage\video_preview.jpg"), QRect(0, 0, element_item.width, element_item.height))
            item = QTreeWidgetItem()
            self.tw_item_preview.addTopLevelItem(item)
            self.tw_item_preview.setItemWidget(item, 0, item_widget)
            item_header = ["images", "name", "format", "frames", "type", "size", "fav", "comment"]
            for each_column in item_header:
                item.setText(item_header.index(each_column), each_column)
            item.setSizeHint(0, QSize(element_item.width, element_item.height))

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

