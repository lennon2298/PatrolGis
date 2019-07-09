from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication, QMainWindow,QFileDialog,QVBoxLayout)
from resource_rc import *
import sys
from parent_ui import Ui_MainWindow
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
        random_col()
        self.ui.figure.clear()
        ax = self.ui.figure.add_subplot(111)
        ax.axis('off')
        for i in range(len(list_of_shp_files)):
            # print(i)
            self.f_name = list_of_shp_files[i]
            self.shape_file = gpd.read_file(self.f_name)
            shp_attributes.append(self.shape_file)
            # CHECK IF THE PROJECT OF THE SHAPEFILE IS SAME OR NOT AND THEN SET IT ACCORDINGLY

            if self.shape_file.crs['init'] != 'epsg:32644':
                print(self.shape_file.crs['init'])
                self.data_proj = self.shape_file.copy()
                self.data_proj['geometry'] = self.data_proj['geometry'].to_crs(epsg=32644)
            else:
                self.data_proj = self.shape_file.copy()
            self.data_proj .plot(categorical=True,
                           ax=ax,
                           color=color_list[i],
                           legend=True,
                           edgecolor='black',
                           figsize=(20, 20),
                           markersize=45
                          )
        self.ui.canvas.draw()

    
    def getfile(self):
            self.fname = QFileDialog.getOpenFileName(self,'Open File','D:\Work\Basemaps\Basemaps',"Shape Files (*.shp)")
            # print(self.fname[0])
            if self.fname is not None:
                list_of_shp_files.append(self.fname[0])
                self.c_plot()

    
    def savefile(self):
            fname = QFileDialog.getSaveFileName(self,'Save File','d:\\',"Shape Files (*.shp)")
    
    def saveasfile(self):
            fname = QFileDialog.getSaveFileName(self,'Save As','d:\\')


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = MyForm()
    mainwin.show()
    sys.exit(app.exec_())