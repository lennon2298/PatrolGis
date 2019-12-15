# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cellDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QDialog)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class Ui_cellDialog(QDialog):
    def setupUi(self, cellDialog):
        cellDialog.setObjectName("cellDialog")
        cellDialog.resize(600, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cellDialog.sizePolicy().hasHeightForWidth())
        cellDialog.setSizePolicy(sizePolicy)
        cellDialog.setMinimumSize(QtCore.QSize(600, 200))
        self.gridLayout = QtWidgets.QGridLayout(cellDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.startLabel = QtWidgets.QLabel(cellDialog)
        self.startLabel.setObjectName("startLabel")
        self.gridLayout.addWidget(self.startLabel, 0, 0, 1, 1)
        self.startCell = QtWidgets.QLineEdit(cellDialog)
        self.startCell.setObjectName("startCell")
        self.gridLayout.addWidget(self.startCell, 0, 1, 1, 1)
        self.endCell = QtWidgets.QLineEdit(cellDialog)
        self.endCell.setObjectName("endCell")
        self.gridLayout.addWidget(self.endCell, 0, 3, 1, 1)
        self.endLabel = QtWidgets.QLabel(cellDialog)
        self.endLabel.setObjectName("endLabel")
        self.gridLayout.addWidget(self.endLabel, 0, 2, 1, 1)
        self.cancelButtonCd = QtWidgets.QPushButton(cellDialog)
        self.cancelButtonCd.setObjectName("cancelButtonCd")
        self.gridLayout.addWidget(self.cancelButtonCd, 1, 3, 1, 1)
        self.okButtonCd = QtWidgets.QPushButton(cellDialog)
        self.okButtonCd.setObjectName("okButtonCd")
        self.gridLayout.addWidget(self.okButtonCd, 1, 2, 1, 1)
        # self.okButtonCd.resize(40,5)
        self.retranslateUi(cellDialog)
        QtCore.QMetaObject.connectSlotsByName(cellDialog)

    def retranslateUi(self, cellDialog):
        _translate = QtCore.QCoreApplication.translate
        cellDialog.setWindowTitle(_translate("cellDialog", "Enter Starting and Ending Station"))
        self.startLabel.setText(_translate("cellDialog", "Starting Patrol Station:"))
        self.endLabel.setText(_translate("cellDialog", "Ending Patrol Station:"))
        self.cancelButtonCd.setText(_translate("cellDialog", "Cancel"))
        self.okButtonCd.setText(_translate("cellDialog", "Ok"))


    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.cal = QDialog(self)


