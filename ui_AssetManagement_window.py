# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AssetManagement_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QButtonGroup, QCalendarWidget,
    QCheckBox, QComboBox, QDockWidget, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1244, 780)
        self.actionshow1 = QAction(MainWindow)
        self.actionshow1.setObjectName(u"actionshow1")
        self.actionshowDock2 = QAction(MainWindow)
        self.actionshowDock2.setObjectName(u"actionshowDock2")
        self.actionshow2 = QAction(MainWindow)
        self.actionshow2.setObjectName(u"actionshow2")
        self.actionhide1 = QAction(MainWindow)
        self.actionhide1.setObjectName(u"actionhide1")
        self.actionhide2 = QAction(MainWindow)
        self.actionhide2.setObjectName(u"actionhide2")
        self.actionshow3 = QAction(MainWindow)
        self.actionshow3.setObjectName(u"actionshow3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        font = QFont()
        font.setPointSize(20)
        self.logo_label.setFont(font)
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.logo_label)

        self.limit_label = QLabel(self.centralwidget)
        self.limit_label.setObjectName(u"limit_label")
        font1 = QFont()
        font1.setPointSize(16)
        self.limit_label.setFont(font1)
        self.limit_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.limit_label)

        self.producer_label = QLabel(self.centralwidget)
        self.producer_label.setObjectName(u"producer_label")
        self.producer_label.setFont(font1)
        self.producer_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.producer_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.project_grpBox = QGroupBox(self.centralwidget)
        self.project_grpBox.setObjectName(u"project_grpBox")
        self.horizontalLayout_7 = QHBoxLayout(self.project_grpBox)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.scrollArea = QScrollArea(self.project_grpBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 491, 99))
        self.project_grpBox_gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.project_grpBox_gridLayout.setSpacing(2)
        self.project_grpBox_gridLayout.setObjectName(u"project_grpBox_gridLayout")
        self.project_grpBox_gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.project_grpBox_gridLayout.setContentsMargins(2, 2, 2, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_7.addWidget(self.scrollArea)


        self.verticalLayout_8.addWidget(self.project_grpBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_8.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_8)

        self.cur_project_name = QLabel(self.centralwidget)
        self.cur_project_name.setObjectName(u"cur_project_name")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.cur_project_name.setFont(font3)
        self.cur_project_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.cur_project_name)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.change_label = QLabel(self.centralwidget)
        self.change_label.setObjectName(u"change_label")

        self.horizontalLayout.addWidget(self.change_label)

        self.change_lineEdit = QLineEdit(self.centralwidget)
        self.change_lineEdit.setObjectName(u"change_lineEdit")

        self.horizontalLayout.addWidget(self.change_lineEdit)


        self.verticalLayout_10.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_xianshi = QLabel(self.centralwidget)
        self.label_xianshi.setObjectName(u"label_xianshi")
        self.label_xianshi.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_xianshi)

        self.mod_btn = QPushButton(self.centralwidget)
        self.msr_btngrp = QButtonGroup(MainWindow)
        self.msr_btngrp.setObjectName(u"msr_btngrp")
        self.msr_btngrp.setExclusive(False)
        self.msr_btngrp.addButton(self.mod_btn)
        self.mod_btn.setObjectName(u"mod_btn")
        self.mod_btn.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u"icons/pic1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.mod_btn.setIcon(icon)
        self.mod_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.mod_btn)

        self.shad_btn = QPushButton(self.centralwidget)
        self.msr_btngrp.addButton(self.shad_btn)
        self.shad_btn.setObjectName(u"shad_btn")
        self.shad_btn.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u"icons/pic2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.shad_btn.setIcon(icon1)
        self.shad_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.shad_btn)

        self.rig_btn = QPushButton(self.centralwidget)
        self.msr_btngrp.addButton(self.rig_btn)
        self.rig_btn.setObjectName(u"rig_btn")
        self.rig_btn.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u"icons/pic4.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.rig_btn.setIcon(icon2)
        self.rig_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.rig_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.search_lineEdit = QLineEdit(self.centralwidget)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.search_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.calendarWgt = QCalendarWidget(self.centralwidget)
        self.calendarWgt.setObjectName(u"calendarWgt")
        self.calendarWgt.setMaximumSize(QSize(16777215, 175))
        self.calendarWgt.setFocusPolicy(Qt.NoFocus)
        self.calendarWgt.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.horizontalLayout_4.addWidget(self.calendarWgt)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 10)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.table_Wgt = QTableWidget(self.groupBox)
        if (self.table_Wgt.columnCount() < 27):
            self.table_Wgt.setColumnCount(27)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_Wgt.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        self.table_Wgt.setObjectName(u"table_Wgt")
        self.table_Wgt.setFocusPolicy(Qt.NoFocus)
        self.table_Wgt.setFrameShadow(QFrame.Plain)
        self.table_Wgt.setLineWidth(0)
        self.table_Wgt.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_Wgt.setAutoScroll(True)
        self.table_Wgt.setAlternatingRowColors(True)
        self.table_Wgt.setRowCount(0)
        self.table_Wgt.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table_Wgt)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget_1 = QDockWidget(MainWindow)
        self.dockWidget_1.setObjectName(u"dockWidget_1")
        self.dockWidget_1.setMinimumSize(QSize(218, 404))
        self.dockWidget_1.setMaximumSize(QSize(218, 404))
        self.dockWidget_1.setFloating(False)
        self.dockWidget_1.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.dockWidgetContents_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.c_groupBox = QGroupBox(self.groupBox_3)
        self.c_groupBox.setObjectName(u"c_groupBox")
        self.gridLayout_2 = QGridLayout(self.c_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hSpacer_11 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.hSpacer_11, 7, 0, 1, 1)

        self.shad_of_CBox = QCheckBox(self.c_groupBox)
        self.shad_of_CBox.setObjectName(u"shad_of_CBox")
        self.shad_of_CBox.setFocusPolicy(Qt.NoFocus)
        self.shad_of_CBox.setChecked(True)

        self.gridLayout_2.addWidget(self.shad_of_CBox, 6, 1, 1, 1)

        self.en_lineEdit = QLineEdit(self.c_groupBox)
        self.en_lineEdit.setObjectName(u"en_lineEdit")

        self.gridLayout_2.addWidget(self.en_lineEdit, 2, 1, 1, 1)

        self.label_5 = QLabel(self.c_groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.hSpacer_9 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.hSpacer_9, 4, 0, 1, 1)

        self.type_cbBox = QComboBox(self.c_groupBox)
        self.type_cbBox.addItem("")
        self.type_cbBox.addItem("")
        self.type_cbBox.addItem("")
        self.type_cbBox.addItem("")
        self.type_cbBox.setObjectName(u"type_cbBox")
        self.type_cbBox.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.type_cbBox, 0, 1, 1, 1)

        self.reset_param_btn = QPushButton(self.c_groupBox)
        self.reset_param_btn.setObjectName(u"reset_param_btn")
        self.reset_param_btn.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.reset_param_btn, 11, 0, 1, 1)

        self.label_2 = QLabel(self.c_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_7 = QLabel(self.c_groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.design_of_CBox = QCheckBox(self.c_groupBox)
        self.design_of_CBox.setObjectName(u"design_of_CBox")
        self.design_of_CBox.setFocusPolicy(Qt.NoFocus)
        self.design_of_CBox.setChecked(True)

        self.gridLayout_2.addWidget(self.design_of_CBox, 4, 1, 1, 1)

        self.hSpacer_12 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.hSpacer_12, 5, 0, 1, 1)

        self.mod_of_CBox = QCheckBox(self.c_groupBox)
        self.mod_of_CBox.setObjectName(u"mod_of_CBox")
        self.mod_of_CBox.setFocusPolicy(Qt.NoFocus)
        self.mod_of_CBox.setChecked(True)

        self.gridLayout_2.addWidget(self.mod_of_CBox, 5, 1, 1, 1)

        self.rig_of_CBox = QCheckBox(self.c_groupBox)
        self.rig_of_CBox.setObjectName(u"rig_of_CBox")
        self.rig_of_CBox.setFocusPolicy(Qt.NoFocus)
        self.rig_of_CBox.setChecked(True)

        self.gridLayout_2.addWidget(self.rig_of_CBox, 7, 1, 1, 1)

        self.create_asset_btn = QPushButton(self.c_groupBox)
        self.create_asset_btn.setObjectName(u"create_asset_btn")
        self.create_asset_btn.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.create_asset_btn, 11, 1, 1, 1)

        self.label_6 = QLabel(self.c_groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.zn_lineEdit = QLineEdit(self.c_groupBox)
        self.zn_lineEdit.setObjectName(u"zn_lineEdit")

        self.gridLayout_2.addWidget(self.zn_lineEdit, 1, 1, 1, 1)

        self.hSpacer_10 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.hSpacer_10, 6, 0, 1, 1)

        self.ep_lineEdit = QLineEdit(self.c_groupBox)
        self.ep_lineEdit.setObjectName(u"ep_lineEdit")

        self.gridLayout_2.addWidget(self.ep_lineEdit, 3, 1, 1, 1)

        self.excel_path_lineEdit = QLineEdit(self.c_groupBox)
        self.excel_path_lineEdit.setObjectName(u"excel_path_lineEdit")
        self.excel_path_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.excel_path_lineEdit, 12, 0, 1, 2)

        self.write_excel_btn = QPushButton(self.c_groupBox)
        self.write_excel_btn.setObjectName(u"write_excel_btn")
        self.write_excel_btn.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_2.addWidget(self.write_excel_btn, 13, 1, 1, 1)

        self.write_sec_btn = QPushButton(self.c_groupBox)
        self.write_sec_btn.setObjectName(u"write_sec_btn")

        self.gridLayout_2.addWidget(self.write_sec_btn, 13, 0, 1, 1)


        self.verticalLayout.addWidget(self.c_groupBox)

        self.detail_plainTextEdit = QPlainTextEdit(self.groupBox_3)
        self.detail_plainTextEdit.setObjectName(u"detail_plainTextEdit")
        self.detail_plainTextEdit.setFocusPolicy(Qt.ClickFocus)
        self.detail_plainTextEdit.setMidLineWidth(0)
        self.detail_plainTextEdit.setProperty("tabStopWidth", 60)

        self.verticalLayout.addWidget(self.detail_plainTextEdit)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.mod_fb_btn = QPushButton(self.groupBox_3)
        self.mod_fb_btn.setObjectName(u"mod_fb_btn")
        self.mod_fb_btn.setFocusPolicy(Qt.NoFocus)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.mod_fb_btn)

        self.shad_fb_btn = QPushButton(self.groupBox_3)
        self.shad_fb_btn.setObjectName(u"shad_fb_btn")
        self.shad_fb_btn.setFocusPolicy(Qt.NoFocus)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.shad_fb_btn)

        self.rig_fb_btn = QPushButton(self.groupBox_3)
        self.rig_fb_btn.setObjectName(u"rig_fb_btn")
        self.rig_fb_btn.setFocusPolicy(Qt.NoFocus)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.rig_fb_btn)

        self.clear_ptext_btn = QPushButton(self.groupBox_3)
        self.clear_ptext_btn.setObjectName(u"clear_ptext_btn")
        self.clear_ptext_btn.setFocusPolicy(Qt.NoFocus)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.clear_ptext_btn)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.dockWidget_1.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget_1)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setMinimumSize(QSize(218, 300))
        self.dockWidget_2.setMaximumSize(QSize(300, 600))
        self.dockWidget_2.setFloating(False)
        self.dockWidget_2.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_2.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout_12 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.dockWidgetContents)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setFocusPolicy(Qt.NoFocus)
        self.tabWidget_2.setTabShape(QTabWidget.Triangular)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.p_tablewgt = QTableWidget(self.tab_3)
        if (self.p_tablewgt.columnCount() < 4):
            self.p_tablewgt.setColumnCount(4)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.p_tablewgt.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.p_tablewgt.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.p_tablewgt.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.p_tablewgt.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        self.p_tablewgt.setObjectName(u"p_tablewgt")
        self.p_tablewgt.setFocusPolicy(Qt.NoFocus)
        self.p_tablewgt.setAlternatingRowColors(True)
        self.p_tablewgt.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.p_tablewgt)

        self.show_producer_btn = QPushButton(self.tab_3)
        self.show_producer_btn.setObjectName(u"show_producer_btn")
        self.show_producer_btn.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_5.addWidget(self.show_producer_btn)

        self.search_lineEdit_1 = QLineEdit(self.tab_3)
        self.search_lineEdit_1.setObjectName(u"search_lineEdit_1")

        self.verticalLayout_5.addWidget(self.search_lineEdit_1)

        self.zp_grpBox = QGroupBox(self.tab_3)
        self.zp_grpBox.setObjectName(u"zp_grpBox")
        self.zp_grpBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.zp_grpBox)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.pos_combox = QComboBox(self.zp_grpBox)
        self.pos_combox.addItem("")
        self.pos_combox.addItem("")
        self.pos_combox.addItem("")
        self.pos_combox.setObjectName(u"pos_combox")
        self.pos_combox.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_10.addWidget(self.pos_combox)

        self.name_lineEdit_2 = QLineEdit(self.zp_grpBox)
        self.name_lineEdit_2.setObjectName(u"name_lineEdit_2")

        self.horizontalLayout_10.addWidget(self.name_lineEdit_2)

        self.tel_lineEdit = QLineEdit(self.zp_grpBox)
        self.tel_lineEdit.setObjectName(u"tel_lineEdit")

        self.horizontalLayout_10.addWidget(self.tel_lineEdit)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 4)
        self.horizontalLayout_10.setStretch(2, 6)

        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.add_producer_btn = QPushButton(self.zp_grpBox)
        self.add_producer_btn.setObjectName(u"add_producer_btn")
        self.add_producer_btn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_11.addWidget(self.add_producer_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.verticalLayout_5.addWidget(self.zp_grpBox)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_12 = QVBoxLayout(self.tab_4)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 3, 3, 3)
        self.history_treeWgt = QTreeWidget(self.tab_4)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.history_treeWgt.setHeaderItem(__qtreewidgetitem)
        self.history_treeWgt.setObjectName(u"history_treeWgt")
        self.history_treeWgt.setFocusPolicy(Qt.NoFocus)
        self.history_treeWgt.setHeaderHidden(True)

        self.verticalLayout_12.addWidget(self.history_treeWgt)

        self.show_htime_btn = QPushButton(self.tab_4)
        self.show_htime_btn.setObjectName(u"show_htime_btn")
        self.show_htime_btn.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_12.addWidget(self.show_htime_btn)

        self.search_lineEdit_2 = QLineEdit(self.tab_4)
        self.search_lineEdit_2.setObjectName(u"search_lineEdit_2")

        self.verticalLayout_12.addWidget(self.search_lineEdit_2)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.horizontalLayout_12.addWidget(self.tabWidget_2)

        self.dockWidget_2.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget_2)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1244, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_3 = QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName(u"dockWidget_3")
        self.dockWidget_3.setFloating(True)
        self.dockWidget_3.setAllowedAreas(Qt.NoDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_13 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.dockWidgetContents_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(1)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setContentsMargins(1, 3, 2, 3)
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_23, 4, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.param1_lineEdit = QLineEdit(self.groupBox_2)
        self.param1_lineEdit.setObjectName(u"param1_lineEdit")
        self.param1_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.param1_lineEdit, 12, 2, 1, 1)

        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_27, 21, 0, 1, 1)

        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_26, 20, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_17, 13, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_24, 5, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_18, 8, 0, 1, 1)

        self.uepath_lineEdit = QLineEdit(self.groupBox_2)
        self.uepath_lineEdit.setObjectName(u"uepath_lineEdit")
        self.uepath_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.uepath_lineEdit, 21, 2, 1, 1)

        self.preview_btn = QPushButton(self.groupBox_2)
        self.preview_btn.setObjectName(u"preview_btn")

        self.gridLayout_4.addWidget(self.preview_btn, 23, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 1, 2, 1, 1)

        self.backup_lineEdit = QLineEdit(self.groupBox_2)
        self.backup_lineEdit.setObjectName(u"backup_lineEdit")
        self.backup_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.backup_lineEdit, 20, 2, 1, 1)

        self.ptype_lineEdit = QLineEdit(self.groupBox_2)
        self.ptype_lineEdit.setObjectName(u"ptype_lineEdit")
        self.ptype_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.ptype_lineEdit, 10, 2, 1, 1)

        self.stype_lineEdit = QLineEdit(self.groupBox_2)
        self.stype_lineEdit.setObjectName(u"stype_lineEdit")
        self.stype_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.stype_lineEdit, 8, 2, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_19, 17, 0, 1, 1)

        self.ep_lineEdit_2 = QLineEdit(self.groupBox_2)
        self.ep_lineEdit_2.setObjectName(u"ep_lineEdit_2")
        self.ep_lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.ep_lineEdit_2, 4, 2, 1, 1)

        self.param2_lineEdit = QLineEdit(self.groupBox_2)
        self.param2_lineEdit.setObjectName(u"param2_lineEdit")
        self.param2_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.param2_lineEdit, 13, 2, 1, 1)

        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_25, 19, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_21, 12, 0, 1, 1)

        self.ctype_lineEdit = QLineEdit(self.groupBox_2)
        self.ctype_lineEdit.setObjectName(u"ctype_lineEdit")
        self.ctype_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.ctype_lineEdit, 5, 2, 1, 1)

        self.mayapath_lineEdit = QLineEdit(self.groupBox_2)
        self.mayapath_lineEdit.setObjectName(u"mayapath_lineEdit")
        self.mayapath_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.mayapath_lineEdit, 22, 2, 1, 1)

        self.param3_lineEdit = QLineEdit(self.groupBox_2)
        self.param3_lineEdit.setObjectName(u"param3_lineEdit")
        self.param3_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.param3_lineEdit, 17, 2, 1, 1)

        self.letter_lineEdit = QLineEdit(self.groupBox_2)
        self.letter_lineEdit.setObjectName(u"letter_lineEdit")
        self.letter_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.letter_lineEdit, 3, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_16, 10, 0, 1, 1)

        self.name_lineEdit = QLineEdit(self.groupBox_2)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.name_lineEdit, 2, 2, 1, 1)

        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)

        self.design_lineEdit = QLineEdit(self.groupBox_2)
        self.design_lineEdit.setObjectName(u"design_lineEdit")
        self.design_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.design_lineEdit, 19, 2, 1, 1)

        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_28, 22, 0, 1, 1)

        self.etype_lineEdit = QLineEdit(self.groupBox_2)
        self.etype_lineEdit.setObjectName(u"etype_lineEdit")
        self.etype_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.etype_lineEdit, 11, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_11, 11, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.dockWidgetContents_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label, 2, 0, 1, 1)

        self.edit_project_btn = QPushButton(self.groupBox_4)
        self.edit_project_btn.setObjectName(u"edit_project_btn")
        self.edit_project_btn.setMaximumSize(QSize(60, 16777215))
        self.edit_project_btn.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.edit_project_btn, 4, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.checkBox, 5, 0, 1, 1)

        self.add_project_btn = QPushButton(self.groupBox_4)
        self.add_project_btn.setObjectName(u"add_project_btn")
        self.add_project_btn.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.add_project_btn, 4, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(60, 16777215))
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)

        self.icon_path_toolBtn = QToolButton(self.groupBox_4)
        self.icon_path_toolBtn.setObjectName(u"icon_path_toolBtn")
        self.icon_path_toolBtn.setMaximumSize(QSize(24, 16777215))
        self.icon_path_toolBtn.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.icon_path_toolBtn, 3, 2, 1, 1)

        self.drop_table_btn = QPushButton(self.groupBox_4)
        self.drop_table_btn.setObjectName(u"drop_table_btn")
        self.drop_table_btn.setEnabled(False)
        self.drop_table_btn.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.drop_table_btn, 5, 1, 1, 1)

        self.leader_lineEdit = QLineEdit(self.groupBox_4)
        self.leader_lineEdit.setObjectName(u"leader_lineEdit")
        self.leader_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.leader_lineEdit, 2, 1, 1, 1)

        self.manager_lineEdit = QLineEdit(self.groupBox_4)
        self.manager_lineEdit.setObjectName(u"manager_lineEdit")
        self.manager_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.manager_lineEdit, 1, 1, 1, 1)

        self.icon_path_lineEdit = QLineEdit(self.groupBox_4)
        self.icon_path_lineEdit.setObjectName(u"icon_path_lineEdit")
        self.icon_path_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.icon_path_lineEdit, 3, 0, 1, 2)


        self.verticalLayout_13.addWidget(self.groupBox_4)

        self.verticalLayout_13.setStretch(0, 3)
        self.verticalLayout_13.setStretch(1, 2)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_3)
#if QT_CONFIG(shortcut)
        self.change_label.setBuddy(self.change_lineEdit)
        self.label_23.setBuddy(self.ep_lineEdit_2)
        self.label_27.setBuddy(self.uepath_lineEdit)
        self.label_26.setBuddy(self.backup_lineEdit)
        self.label_17.setBuddy(self.param2_lineEdit)
        self.label_24.setBuddy(self.ctype_lineEdit)
        self.label_18.setBuddy(self.stype_lineEdit)
        self.label_19.setBuddy(self.param3_lineEdit)
        self.label_25.setBuddy(self.design_lineEdit)
        self.label_21.setBuddy(self.param1_lineEdit)
        self.label_16.setBuddy(self.ptype_lineEdit)
        self.label_22.setBuddy(self.name_lineEdit)
        self.label_28.setBuddy(self.mayapath_lineEdit)
        self.label.setBuddy(self.leader_lineEdit)
        self.label_20.setBuddy(self.manager_lineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.change_lineEdit, self.search_lineEdit)
        QWidget.setTabOrder(self.search_lineEdit, self.search_lineEdit_1)
        QWidget.setTabOrder(self.search_lineEdit_1, self.name_lineEdit_2)
        QWidget.setTabOrder(self.name_lineEdit_2, self.tel_lineEdit)
        QWidget.setTabOrder(self.tel_lineEdit, self.name_lineEdit)
        QWidget.setTabOrder(self.name_lineEdit, self.letter_lineEdit)
        QWidget.setTabOrder(self.letter_lineEdit, self.ep_lineEdit_2)
        QWidget.setTabOrder(self.ep_lineEdit_2, self.ctype_lineEdit)
        QWidget.setTabOrder(self.ctype_lineEdit, self.stype_lineEdit)
        QWidget.setTabOrder(self.stype_lineEdit, self.ptype_lineEdit)
        QWidget.setTabOrder(self.ptype_lineEdit, self.param1_lineEdit)
        QWidget.setTabOrder(self.param1_lineEdit, self.param2_lineEdit)
        QWidget.setTabOrder(self.param2_lineEdit, self.param3_lineEdit)
        QWidget.setTabOrder(self.param3_lineEdit, self.design_lineEdit)
        QWidget.setTabOrder(self.design_lineEdit, self.backup_lineEdit)
        QWidget.setTabOrder(self.backup_lineEdit, self.uepath_lineEdit)
        QWidget.setTabOrder(self.uepath_lineEdit, self.mayapath_lineEdit)
        QWidget.setTabOrder(self.mayapath_lineEdit, self.manager_lineEdit)
        QWidget.setTabOrder(self.manager_lineEdit, self.leader_lineEdit)
        QWidget.setTabOrder(self.leader_lineEdit, self.icon_path_lineEdit)
        QWidget.setTabOrder(self.icon_path_lineEdit, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.drop_table_btn)
        QWidget.setTabOrder(self.drop_table_btn, self.search_lineEdit_2)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.actionshow1)
        self.menu_2.addAction(self.actionshow2)
        self.menu_3.addAction(self.actionshow3)

        self.retranslateUi(MainWindow)
        self.actionshow1.triggered.connect(self.dockWidget_1.show)
        self.actionshow2.triggered.connect(self.dockWidget_2.show)
        self.actionhide1.triggered.connect(self.dockWidget_1.hide)
        self.actionhide2.triggered.connect(self.dockWidget_2.hide)
        self.clear_ptext_btn.clicked.connect(self.detail_plainTextEdit.clear)
        self.checkBox.clicked["bool"].connect(self.drop_table_btn.setEnabled)
        self.actionshow3.triggered.connect(self.dockWidget_3.show)

        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionshow1.setText(QCoreApplication.translate("MainWindow", u"show", None))
        self.actionshowDock2.setText(QCoreApplication.translate("MainWindow", u"show_Dock2", None))
        self.actionshow2.setText(QCoreApplication.translate("MainWindow", u"show", None))
        self.actionhide1.setText(QCoreApplication.translate("MainWindow", u"hide", None))
        self.actionhide2.setText(QCoreApplication.translate("MainWindow", u"hide", None))
        self.actionshow3.setText(QCoreApplication.translate("MainWindow", u"show", None))
        self.logo_label.setText(QCoreApplication.translate("MainWindow", u"t", None))
        self.limit_label.setText(QCoreApplication.translate("MainWindow", u"\u6743\u9650", None))
        self.producer_label.setText(QCoreApplication.translate("MainWindow", u"\u67d0\u67d0\u67d0", None))
        self.project_grpBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u9009\u62e9", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u9879\u76ee\u4e3a:", None))
        self.cur_project_name.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u9879\u76ee", None))
        self.change_label.setText(QCoreApplication.translate("MainWindow", u"\u591a\u9879\u4fee\u6539", None))
        self.change_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u591a\u9879\u4fee\u6539\u7684\u5185\u5bb9", None))
        self.label_xianshi.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u4e0e\u53d1\u5e03", None))
        self.mod_btn.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.shad_btn.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28", None))
        self.rig_btn.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u667a\u80fd\u641c\u7d22", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u90e8\u5206\u5217\u8868\u641c\u7d22", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8d44\u4ea7\u4efb\u52a1\u8868", None))
        ___qtablewidgetitem = self.table_Wgt.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.table_Wgt.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u73b0\u96c6\u6570", None));
        ___qtablewidgetitem2 = self.table_Wgt.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem3 = self.table_Wgt.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\u540d", None));
        ___qtablewidgetitem4 = self.table_Wgt.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u82f1\u6587\u540d", None));
        ___qtablewidgetitem5 = self.table_Wgt.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u8ba1\u7a3f", None));
        ___qtablewidgetitem6 = self.table_Wgt.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8fdb\u5ea6", None));
        ___qtablewidgetitem7 = self.table_Wgt.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5206\u914d", None));
        ___qtablewidgetitem8 = self.table_Wgt.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5efa\u8bae\u65f6\u95f4", None));
        ___qtablewidgetitem9 = self.table_Wgt.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7ed3\u675f", None));
        ___qtablewidgetitem10 = self.table_Wgt.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5269\u4f59", None));
        ___qtablewidgetitem11 = self.table_Wgt.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u53cd\u9988", None));
        ___qtablewidgetitem12 = self.table_Wgt.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7248\u672c", None));
        ___qtablewidgetitem13 = self.table_Wgt.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28\u8fdb\u5ea6", None));
        ___qtablewidgetitem14 = self.table_Wgt.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28\u5206\u914d", None));
        ___qtablewidgetitem15 = self.table_Wgt.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28\u5efa\u8bae\u65f6\u95f4", None));
        ___qtablewidgetitem16 = self.table_Wgt.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28\u7ed3\u675f", None));
        ___qtablewidgetitem17 = self.table_Wgt.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28\u5269\u4f59", None));
        ___qtablewidgetitem18 = self.table_Wgt.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28\u53cd\u9988", None));
        ___qtablewidgetitem19 = self.table_Wgt.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28\u7248\u672c", None));
        ___qtablewidgetitem20 = self.table_Wgt.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a\u8fdb\u5ea6", None));
        ___qtablewidgetitem21 = self.table_Wgt.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a\u5206\u914d", None));
        ___qtablewidgetitem22 = self.table_Wgt.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a\u5efa\u8bae\u65f6\u95f4", None));
        ___qtablewidgetitem23 = self.table_Wgt.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a\u7ed3\u675f", None));
        ___qtablewidgetitem24 = self.table_Wgt.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a\u5269\u4f59", None));
        ___qtablewidgetitem25 = self.table_Wgt.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a\u53cd\u9988", None));
        ___qtablewidgetitem26 = self.table_Wgt.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a\u7248\u672c", None));
        self.groupBox_3.setTitle("")
        self.c_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u8d44\u4ea7", None))
        self.shad_of_CBox.setText(QCoreApplication.translate("MainWindow", u"\u6750\u8d28", None))
        self.en_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u82f1\u6587\u540d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u82f1\u6587\u540d", None))
        self.type_cbBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u89d2\u8272", None))
        self.type_cbBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u9053\u5177", None))
        self.type_cbBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u573a\u666f", None))
        self.type_cbBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5143\u7d20", None))

        self.reset_param_btn.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u53c2\u6570", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u96c6\u6570", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\u540d", None))
        self.design_of_CBox.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u8ba1\u7a3f", None))
        self.mod_of_CBox.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.rig_of_CBox.setText(QCoreApplication.translate("MainWindow", u"\u7ed1\u5b9a", None))
        self.create_asset_btn.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u8d44\u4ea7", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None))
        self.zn_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\u540d", None))
        self.ep_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u96c6\u6570", None))
        self.excel_path_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8f6c\u5199\u5165\u8868\u683c\u8def\u5f84(\u5b8c\u6574)", None))
        self.write_excel_btn.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u5230\u8868\u683c", None))
        self.write_sec_btn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u4e2d\u884c\u8f93\u51fa", None))
        self.detail_plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u90e8\u5206\u8be6\u7ec6\u4fe1\u606f,\u4e0d\u8d85\u8fc7100\u5b57", None))
        self.mod_fb_btn.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165\u5230\u6a21\u578b\u53cd\u9988", None))
        self.shad_fb_btn.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165\u5230\u6750\u8d28\u53cd\u9988", None))
        self.rig_fb_btn.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165\u5230\u7ed1\u5b9a\u53cd\u9988", None))
        self.clear_ptext_btn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5185\u5bb9", None))
        ___qtablewidgetitem27 = self.p_tablewgt.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem28 = self.p_tablewgt.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem29 = self.p_tablewgt.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8bdd", None));
        ___qtablewidgetitem30 = self.p_tablewgt.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u804c\u4f4d", None));
        self.show_producer_btn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.search_lineEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u8981\u67e5\u627e\u7684\u76ee\u6807,\u56de\u8f66\u9009\u62e9", None))
        self.zp_grpBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4eba\u5458", None))
        self.pos_combox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7ec4\u5458", None))
        self.pos_combox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7ec4\u957f", None))
        self.pos_combox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5236\u7247", None))

        self.name_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.tel_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7535\u8bdd(\u9489\u9489\u4e2d\u7684)", None))
        self.add_producer_btn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4eba\u5458", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u4eba\u5458\u540d\u5355", None))
        self.show_htime_btn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.search_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u8981\u67e5\u627e\u7684\u76ee\u6807,\u56de\u8f66\u9009\u62e9", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u5386\u53f2\u65f6\u95f4", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u8d44\u4ea7", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u4eba\u5458\u540d\u5355/\u5386\u53f2\u65f6\u95f4", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u9879\u76ee/\u7f16\u8f91\u9879\u76ee", None))
        self.dockWidget_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u7a97\u53e3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u89c4\u5219", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u5206\u96c6\u540d{ep}", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u96c6\u6570{num}", None))
        self.param1_lineEdit.setText("")
        self.param1_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\u53ef\u4e3a\u7a7a)", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"UE\u8def\u5f84", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u9988\u8def\u5f84", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u76d8\u7b26{letter}", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u65702{param2}", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u540d{type}", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u573a\u666f\u540d{type}", None))
        self.uepath_lineEdit.setText(QCoreApplication.translate("MainWindow", u"{letter}:/{proj}_Project/05_UE4/{type}/{name}", None))
        self.uepath_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u8def\u5f84\u7684\u7b26\u53f7", None))
        self.preview_btn.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8\u8def\u5f84", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u4ea7\u540d\u79f0{name}(\u522b\u6f0f\u4e86)", None))
        self.backup_lineEdit.setText(QCoreApplication.translate("MainWindow", u"{letter}:/{proj}_Project/01_documents/check/{type}/{name}", None))
        self.backup_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4ee5\u4e0a\u4e3a\u66ff\u6362\u5185\u5bb9", None))
        self.ptype_lineEdit.setText(QCoreApplication.translate("MainWindow", u"props", None))
        self.ptype_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9053\u5177\u7c7b\u540dprop", None))
        self.stype_lineEdit.setText(QCoreApplication.translate("MainWindow", u"scenes", None))
        self.stype_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u573a\u666f\u7c7b\u540dscene", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u65703{param3}", None))
        self.ep_lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"ep", None))
        self.ep_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ep", None))
        self.param2_lineEdit.setText("")
        self.param2_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\u53ef\u4e3a\u7a7a)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u8ba1\u7a3f\u8def\u5f84", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u65701{param1}", None))
        self.ctype_lineEdit.setText(QCoreApplication.translate("MainWindow", u"characters", None))
        self.ctype_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u7c7b\u540dcharacter", None))
        self.mayapath_lineEdit.setText(QCoreApplication.translate("MainWindow", u"{letter}:/{proj}_Project/03_main_prodution/ep000/assets/{type}/{name}", None))
        self.mayapath_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5c3d\u91cf\u7528/,\u4e0d\u7528\\", None))
        self.param3_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\u53ef\u4e3a\u7a7a)", None))
        self.letter_lineEdit.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u9053\u5177\u540d{type}", None))
        self.name_lineEdit.setText("")
        self.name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5b57\u6bcd,\u6ce8\u610f\u5927\u5c0f\u5199", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u540d{proj}", None))
        self.design_lineEdit.setText(QCoreApplication.translate("MainWindow", u"{letter}:/{proj}_Project/01_documents/design/{type}/{name}", None))
        self.design_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\u4e8b\u9879", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u4ea7\u8def\u5f84", None))
        self.etype_lineEdit.setText(QCoreApplication.translate("MainWindow", u"env", None))
        self.etype_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u573a\u666f\u5143\u7d20\u7c7b\u540denv", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u573a\u666f\u5143\u7d20{type}", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u521b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u957f", None))
        self.edit_project_btn.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u9879\u76ee", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u614e\u70b9!!", None))
        self.add_project_btn.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5236\u7247", None))
        self.icon_path_toolBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.drop_table_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664(\u53ea\u9700\u540d\u79f0)", None))
        self.leader_lineEdit.setText("")
        self.manager_lineEdit.setText("")
        self.manager_lineEdit.setPlaceholderText("")
        self.icon_path_lineEdit.setText("")
        self.icon_path_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u56fe\u6807\u8def\u5f84", None))
    # retranslateUi

