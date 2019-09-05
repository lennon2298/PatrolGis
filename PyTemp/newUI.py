# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QGridLayout, QSizePolicy, QInputDialog, QFileSystemModel, QTreeView, QAbstractItemView)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QDir, Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 723)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/res/mainLogo4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 265))
        self.frame_2.setMaximumSize(QtCore.QSize(388, 500))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 178, 270))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # self.listWidget_3 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        # self.listWidget_3.setObjectName("listWidget_3")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(200, 265))
        self.frame.setMaximumSize(QtCore.QSize(388, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 178, 270))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget.setObjectName("listWidget")
        self.model = QFileSystemModel()
        self.model.setRootPath("D:\Work\PatrolGIS\PatrolGis")
        self.view=QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.view.setModel(self.model)
        self.view.setRootIndex(self.model.index("D:\Work\PatrolGIS\PatrolGis"))
        self.view.setDragEnabled(True)
        self.view.setDragDropMode(QAbstractItemView.InternalMove)
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.horizontalLayout_5.addWidget(self.view)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(600, 608))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        # self.graphicsView = QtWidgets.QGraphicsView(self.frame_3)
        # self.graphicsView.setMinimumSize(QtCore.QSize(580, 445))
        # self.graphicsView.setObjectName("graphicsView")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.frame_3)
        self.canvas.setMinimumSize(QtCore.QSize(570, 435))
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding))
        self.gridLayout_4.addWidget(self.canvas, 1, 0, 1, 1)
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)
        # self.frame_5 = QtWidgets.QFrame(self.frame_3)
        # self.frame_5.setMinimumSize(QtCore.QSize(0, 94))
        # self.frame_5.setMaximumSize(QtCore.QSize(16777215, 135))
        # self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_5.setObjectName("frame_5")
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.scrollArea_3 = QtWidgets.QScrollArea(self.frame_5)
        # self.scrollArea_3.setWidgetResizable(True)
        # self.scrollArea_3.setObjectName("scrollArea_3")
        # self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 558, 113))
        # self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        # self.tableWidget.setMinimumSize(QtCore.QSize(0, 65))
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(0)
        # self.tableWidget.setRowCount(0)
        # self.horizontalLayout_3.addWidget(self.tableWidget)
        # self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        # self.horizontalLayout_2.addWidget(self.scrollArea_3)
        # self.gridLayout_4.addWidget(self.frame_5, 4, 0, 1, 1)
        # self.label_3 = QtWidgets.QLabel(self.frame_3)
        # self.label_3.setObjectName("label_3")
        # self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 1, 1, 2, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(800, 32))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/res/open2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton.setIcon(icon1)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.saveButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/res/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon2)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.saveasButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.saveasButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/res/saveas.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveasButton.setIcon(icon3)
        self.saveasButton.setObjectName("saveasButton")
        self.horizontalLayout.addWidget(self.saveasButton)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        # self.graphicsView = QtWidgets.QGraphicsView(self.frame_3)
        # self.graphicsView.setMinimumSize(QtCore.QSize(580, 445))
        # self.graphicsView.setObjectName("graphicsView")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuPatrolling = QtWidgets.QMenu(self.menubar)
        self.menuPatrolling.setObjectName("menuPatrolling")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPatrolling.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuCreatePath=QtWidgets.QAction(MainWindow)
        self.menuCreatePath.setObjectName("menuCreatePath")
        self.menuSplit=QtWidgets.QAction(MainWindow)
        self.menuSplit.setObjectName("menuSplit")
        self.menuPatrolling.addAction(self.menuSplit)
        self.menuPatrolling.addAction(self.menuCreatePath)
        self.retranslateUi(MainWindow)
        # self.label.setDragEnabled(True)
        # self.label_2.setDragEnabled(True)
        # self.label_3.setDragEnabled(True)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PatrolGIS"))
        self.label_2.setText(_translate("MainWindow", "Layers"))
        self.label.setText(_translate("MainWindow", "Explorer"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuPatrolling.setTitle(_translate("MainWindow", "Patrolling"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuCreatePath.setText(_translate("MainWindow", "Generate Path"))
        self.menuSplit.setText(_translate("MainWindow", "Split into Beats"))

import resource_rc