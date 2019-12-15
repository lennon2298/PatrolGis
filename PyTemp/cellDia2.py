# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cellDialog2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QDialog)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class Ui_cellDialog2(QDialog):
    def setupUi(self, cellDialog2):
        cellDialog2.setObjectName("cellDialog2")
        cellDialog2.resize(400, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cellDialog2.sizePolicy().hasHeightForWidth())
        cellDialog2.setSizePolicy(sizePolicy)
        cellDialog2.setMinimumSize(QtCore.QSize(400, 200))
        self.gridLayout = QtWidgets.QGridLayout(cellDialog2)
        self.gridLayout.setObjectName("gridLayout")
        self.startLabel = QtWidgets.QLabel(cellDialog2)
        self.startLabel.setObjectName("startLabel")
        self.gridLayout.addWidget(self.startLabel, 0, 0, 1, 1)
        self.startCell = QtWidgets.QLineEdit(cellDialog2)
        self.startCell.setObjectName("startCell")
        self.gridLayout.addWidget(self.startCell, 0, 1, 1, 1)
        self.endCell = QtWidgets.QLineEdit(cellDialog2)
        self.endCell.setObjectName("endCell")
        self.gridLayout.addWidget(self.endCell, 0, 3, 1, 1)
        self.endLabel = QtWidgets.QLabel(cellDialog2)
        self.endLabel.setObjectName("endLabel")
        self.gridLayout.addWidget(self.endLabel, 0, 2, 1, 1)
        self.cancelButtonCd2 = QtWidgets.QPushButton(cellDialog2)
        self.cancelButtonCd2.setObjectName("cancelButtonCd2")
        self.gridLayout.addWidget(self.cancelButtonCd2, 1, 3, 1, 1)
        self.okButtonCd2 = QtWidgets.QPushButton(cellDialog2)
        self.okButtonCd2.setObjectName("okButtonCd2")
        self.gridLayout.addWidget(self.okButtonCd2, 1, 2, 1, 1)
        # self.okButtonCd2.resize(40,5)
        self.retranslateUi(cellDialog2)
        QtCore.QMetaObject.connectSlotsByName(cellDialog2)

    def retranslateUi(self, cellDialog2):
        _translate = QtCore.QCoreApplication.translate
        cellDialog2.setWindowTitle(_translate("cellDialog2", "Enter Starting Station  and Total Distance"))
        self.startLabel.setText(_translate("cellDialog2", "Starting Patrol Station:"))
        self.endLabel.setText(_translate("cellDialog2", "Distance:"))
        self.cancelButtonCd2.setText(_translate("cellDialog2", "Cancel"))
        self.okButtonCd2.setText(_translate("cellDialog2", "Ok"))


    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.cal = QDialog(self)


