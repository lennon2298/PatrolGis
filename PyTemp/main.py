from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication, QMainWindow,QFileDialog,QTableWidget,QTableWidgetItem,QListWidgetItem,QListWidget)
from resource_rc import *
import sys
from newUI import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import geopandas as gpd
import os
import earthpy as et
import random
from gis.template import *

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.openButton.clicked.connect(self.getfile)
        self.ui.saveButton.clicked.connect(self.savefile)
        self.ui.saveasButton.clicked.connect(self.saveasfile)
        
    def c_plot(self):
        # self.f_name = name
        # print(self.f_name)
        shp_attributes.clear()
        random_col()
        self.ui.figure.clear()
        ax = self.ui.figure.add_subplot(111)
        ax.axis('off')
        try:
            for i in range(len(list_of_shp_files)):
                # print(i)
                self.f_name = list_of_shp_files[i]
                self.shape_file = gpd.read_file(self.f_name)
                # self.yaga= list()
                shp_attributes.append(self.shape_file)
                # print(self.yaga)
                # shp_attributes.append(self.yaga)
                # print(self.shape_file)
                # print(self.yaga)
                # CHECK IF THE PROJECT OF THE SHAPEFILE IS SAME OR NOT AND THEN SET IT ACCORDINGLY

                if self.shape_file.crs['init'] != 'epsg:32644':
                    # print(self.shape_file.crs['init'])
                    self.data_proj = self.shape_file.copy()
                    self.data_proj['geometry'] = self.data_proj['geometry'].to_crs(epsg=32644)
                else:
                    self.data_proj = self.shape_file.copy()
                self.data_proj .plot(categorical=True,
                               ax=ax,
                               color=color_list[i],
                               legend=True,
                               edgecolor='black',
                               figsize=(60, 60),
                               markersize=45
                              )
        except:
            #print("ERROR!!!")
            del list_of_shp_files[-1]
        self.ui.canvas.draw()

    
    def getfile(self):

            try:
                #self.fname = ""
                self.fname = QFileDialog.getOpenFileName(self,'Open File','D:\Work\Basemaps\Basemaps',"Shape Files (*.shp)")
                #print(self.fname[0])
                if self.fname is not None:
                    if self.fname[0] != "":
                        list_of_shp_files.append(self.fname[0])
                        # shp_attributes.append(self.shape_file[0])
                        #print("XD")
                        self.c_plot()
                        self.get_table()
                        # self.ui.listWidget.setCurrentItem(shp_attributes)
            except:
                print(sys.exc_info()[0], "Exception Caught")
                        
    def savefile(self):
            try:
                fname = QFileDialog.getSaveFileName(self,'Save File','d:\\',"Shape Files (*.shp)")
            except:
                print(sys.exc_info()[0], "Excpetion Caught")
    
    def saveasfile(self):
            try:
                fname = QFileDialog.getSaveFileName(self,'Save As','d:\\')
            except:
                print(sys.exc_info()[0], "Excpetion Caught")

    def get_table(self):
            # self.ui.tableWidget.setRowCount(4)
            self.ui.tableWidget.setColumnCount(1)
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(list_of_shp_files)
            self.ui.listWidget_3.clear()
            self.ui.listWidget_3.addItems(self.shape_file)
            # self.ui.tableWidget.setColumnCount(self.shape_file.colCount())
            # self.ui.tableWidget.setRowCount(self.shape_file.rowCount())
            rowPos=self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPos)

            # self.ui.tableWidget.addItems(self.shape_file) 
            # print(shp_attributes)
            self.ui.tableWidget.setItem(rowPos,0,QTableWidgetItem(str(shp_attributes[0])))
            # self.ui.tableWidget.setItem(rowPos,0,QTableWidgetItem(shp_attributes)
            # self.ui.tableWidget.setItem(1,0, QTableWidgetItem(self.shape_file.readline())
            # self.ui.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
            # self.ui.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
            # self.ui.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
            # self.ui.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
            # self.ui.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
            


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = MyForm()
    mainwin.show()
    sys.exit(app.exec_())