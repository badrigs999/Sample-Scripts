# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'element_browser.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(957, 553)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_ele_name = QComboBox(Form)
        self.cb_ele_name.addItem("")
        self.cb_ele_name.addItem("")
        self.cb_ele_name.setObjectName(u"cb_ele_name")

        self.horizontalLayout.addWidget(self.cb_ele_name)

        self.tb_ele_add = QToolButton(Form)
        self.tb_ele_add.setObjectName(u"tb_ele_add")

        self.horizontalLayout.addWidget(self.tb_ele_add)

        self.tb_ele_remove = QToolButton(Form)
        self.tb_ele_remove.setObjectName(u"tb_ele_remove")

        self.horizontalLayout.addWidget(self.tb_ele_remove)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lw_ele_sub_name = QListWidget(Form)
        QListWidgetItem(self.lw_ele_sub_name)
        QListWidgetItem(self.lw_ele_sub_name)
        self.lw_ele_sub_name.setObjectName(u"lw_ele_sub_name")
        self.lw_ele_sub_name.setMaximumSize(QSize(256, 16777215))

        self.verticalLayout.addWidget(self.lw_ele_sub_name)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hslider_grid = QSlider(Form)
        self.hslider_grid.setObjectName(u"hslider_grid")
        self.hslider_grid.setMaximumSize(QSize(100, 16777215))
        self.hslider_grid.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid rgb(52, 103, 146);\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    }\n"
"QSlider::groove:vertical {\n"
"            background: rgb(52, 103, 146);\n"
"            border: 1px solid rgb(52, 103, 146);\n"
"            width: 10px;\n"
"            margin: 0px;\n"
"        }\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(52, 103, 146);\n"
"    border: 1px solid rgb(52, 103, 146);\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"    }\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(52, 103, 146);\n"
"    border: 1px solid rgb(52, 103, 146);\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"}\n"
"")
        self.hslider_grid.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.hslider_grid)

        self.tb_view = QToolButton(Form)
        self.tb_view.setObjectName(u"tb_view")

        self.horizontalLayout_2.addWidget(self.tb_view)

        self.tb_refresh = QToolButton(Form)
        self.tb_refresh.setObjectName(u"tb_refresh")

        self.horizontalLayout_2.addWidget(self.tb_refresh)

        self.tb_fav = QToolButton(Form)
        self.tb_fav.setObjectName(u"tb_fav")

        self.horizontalLayout_2.addWidget(self.tb_fav)

        self.cb_field = QComboBox(Form)
        self.cb_field.addItem("")
        self.cb_field.addItem("")
        self.cb_field.addItem("")
        self.cb_field.addItem("")
        self.cb_field.addItem("")
        self.cb_field.setObjectName(u"cb_field")

        self.horizontalLayout_2.addWidget(self.cb_field)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.cb_condition = QComboBox(Form)
        self.cb_condition.addItem("")
        self.cb_condition.addItem("")
        self.cb_condition.setObjectName(u"cb_condition")

        self.horizontalLayout_3.addWidget(self.cb_condition)

        self.le_search = QLineEdit(Form)
        self.le_search.setObjectName(u"le_search")

        self.horizontalLayout_3.addWidget(self.le_search)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lb_status = QLabel(Form)
        self.lb_status.setObjectName(u"lb_status")

        self.horizontalLayout_3.addWidget(self.lb_status)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lw_img_preview = QListWidget(Form)
        self.lw_img_preview.setObjectName(u"lw_img_preview")

        self.horizontalLayout_4.addWidget(self.lw_img_preview)

        self.tw_item_preview = QTreeWidget(Form)
        self.tw_item_preview.setObjectName(u"tw_item_preview")

        self.horizontalLayout_4.addWidget(self.tw_item_preview)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.tb_home = QToolButton(Form)
        self.tb_home.setObjectName(u"tb_home")

        self.horizontalLayout_6.addWidget(self.tb_home)

        self.tb_ingest = QToolButton(Form)
        self.tb_ingest.setObjectName(u"tb_ingest")

        self.horizontalLayout_6.addWidget(self.tb_ingest)

        self.tb_settings = QToolButton(Form)
        self.tb_settings.setObjectName(u"tb_settings")

        self.horizontalLayout_6.addWidget(self.tb_settings)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cb_ele_name.setItemText(0, QCoreApplication.translate("Form", u"production", None))
        self.cb_ele_name.setItemText(1, QCoreApplication.translate("Form", u"comp", None))

        self.tb_ele_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.tb_ele_remove.setText(QCoreApplication.translate("Form", u"--", None))

        __sortingEnabled = self.lw_ele_sub_name.isSortingEnabled()
        self.lw_ele_sub_name.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_ele_sub_name.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"fire", None));
        ___qlistwidgetitem1 = self.lw_ele_sub_name.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"smoke", None));
        self.lw_ele_sub_name.setSortingEnabled(__sortingEnabled)

        self.tb_view.setText(QCoreApplication.translate("Form", u"View", None))
        self.tb_refresh.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.tb_fav.setText(QCoreApplication.translate("Form", u"Fav", None))
        self.cb_field.setItemText(0, QCoreApplication.translate("Form", u"name", None))
        self.cb_field.setItemText(1, QCoreApplication.translate("Form", u"format", None))
        self.cb_field.setItemText(2, QCoreApplication.translate("Form", u"frames", None))
        self.cb_field.setItemText(3, QCoreApplication.translate("Form", u"type", None))
        self.cb_field.setItemText(4, QCoreApplication.translate("Form", u"comment", None))

        self.cb_condition.setItemText(0, QCoreApplication.translate("Form", u"contains", None))
        self.cb_condition.setItemText(1, QCoreApplication.translate("Form", u"in", None))

        self.lb_status.setText(QCoreApplication.translate("Form", u"fire: 20 Elements (728mb)", None))
        ___qtreewidgetitem = self.tw_item_preview.headerItem()
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("Form", u"Comment", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("Form", u"Fav", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("Form", u"Size", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Form", u"Type", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"Frames", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Format", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Name", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Preview", None));
        self.tb_home.setText(QCoreApplication.translate("Form", u"Home", None))
        self.tb_ingest.setText(QCoreApplication.translate("Form", u"Ingest", None))
        self.tb_settings.setText(QCoreApplication.translate("Form", u"Settings", None))
    # retranslateUi

