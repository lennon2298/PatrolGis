from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication, QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem, QListWidgetItem, QListWidget, QInputDialog, QAbstractItemView, QMessageBox, QFileSystemModel, QTreeView)
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QPixmap
from resource_rc import *
import sys
from newUI import Ui_MainWindow
from cellDialog import Ui_cellDialog
from pathDia import Ui_Dialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import geopandas as gpd
import os
from matplotlib import cm as cmaps
# import earthpy as et
import random
from gis.template import *
from gis.split import *
from gis.test import *
from gis.algo import *
from gis.shapefile_to_geojson import *
import fiona
import matplotlib.image as mpimg
import os.path
from shapely.geometry import Polygon

class MyForm(QMainWindow):

    # VARIABLES

    __text = int()
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.openButton.clicked.connect(self.getFile)
        self.ui.saveButton.clicked.connect(self.savefile)
        self.ui.saveasButton.clicked.connect(self.saveasfile)
        self.ui.menuCreatePath.triggered.connect(self.showDialog)
        self.ui.menuSplit.triggered.connect(self.create_grid)
        self.setAcceptDrops(True)
        # self.setDragDropMode(QAbstractItemView.InternalMove)
        # self.ui.setAcceptDrops(True)
        self.ui.frame_3.setAcceptDrops(True)
        self.cd = Ui_cellDialog(self)
        self.pd = Ui_Dialog(self)
        # print(self.cd.startCell.text())
        # print(self.cd.endCell.text())
        self.cd.okButtonCd.clicked.connect(self.get_path_with_grid)
        self.cd.cancelButtonCd.clicked.connect(self.cd.close)
        self.pd.pushButton.clicked.connect(self.showCellDialog)
        
        # self.ui.setDragDropMode(QAbstractItemView.InternalMove)

     # INIT BEAT FILE SPLIT    
    def split_beat(self):
        try:
            if list_of_shp_files is None:
                raise ValueError("Please upload a file")
            else:
                self.f_name = list_of_shp_files[len(list_of_shp_files)-1]
                if "BEAT.shp" in self.f_name:
                    self.beat = SplitBeatFile(self.f_name)
                    self.beat.cal_area()
                    self.beat.split()
                    print("Split done right")
                    ok = QMessageBox.about(self, ' ', "Beats Successfully Split")
                    # ok.setIcon(QMessageBox.Information)
                    # msg.setText("Beats Successfully Split!")
                    # msg.show()
                else:
                    raise ValueError("No BEAT file") 
                    
        except ValueError as e:
            print(e)
            ok = QMessageBox.about(self, ' ', "No BEAT file")
        except:
            print("Something went wrong, Try uploading a BEAT file")
            ok = QMessageBox.about(self, "Something Went Wrong", "Try uploading a BEAT file")

    def display_beat(self):
        try:
            matchers = ["BEAT.shp", "Wireless_station.shp"]
            matching = [s for s in list_of_shp_files if any(xs in s for xs in matchers)]
            if matching is None or len(matching)==0:
                raise ValueError("Please upload 'BEAT.shp' and 'Wireless_station.shp'.")
            else:
                file_json = SaveToGeoJSON()
                for i in matching:
                    file_save_name = file_json.file_name()
                    file_json.save(i, file_save_name)
                print("files saved")
                merge_obj = MergeGeoJSON()
                merge_obj.save()
                print("File merged")
                # ok = QMessageBox.about(self, ' ', "File saved")
        except ValueError as e:
            print(e)

    def create_grid(self):
        f_name = list_of_shp_files[-1]
        print(f_name)
        poly = gpd.read_file(f_name)
        # print(poly['geometry'][0].coords.xy)
        global xmin,ymin,xmax,ymax
        xmin,ymin,xmax,ymax = poly.total_bounds
        print(xmin,ymin,xmax,ymax,length,width)
        rows = int(np.ceil((ymax-ymin) /  length))
        cols = int(np.ceil((xmax-xmin) / width))
        XleftOrigin = xmin
        XrightOrigin = xmin + width
        YtopOrigin = ymax
        YbottomOrigin = ymax- length
        polygons = []
        # new = []
        print(type(grid_mat))
        for i in range(cols):
            Ytop = YtopOrigin
            Ybottom =YbottomOrigin
            for j in range(rows):
                polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
                Ytop = Ytop - length
                Ybottom = Ybottom - length
                # new.append(0)
                grid_mat[j][i] = 0
            XleftOrigin = XleftOrigin + width
            XrightOrigin = XrightOrigin + width
            # grid_mat.append(new)
        
        print(len(grid_mat))
        print(len(grid_mat[0]))
        print(rows, cols)
        f_data = open("data1.txt", "w+")
        f_data.write(str(grid_mat))
        f_data.close()

        grid = gpd.GeoDataFrame({'geometry':polygons})
        # grid.to_file('grid.shp')
        # grid['geometry'] = grid['geometry'].to_crs(epsg=32644)
        grid.crs = {'init' :'epsg:4326'}
        grid.to_file('./grid.shp')
        print("here")
        # print(grid)
        # list_of_shp_files.append('./grid.shp')
        # self.c_plot()
        # self.get_table()

    def get_cell(self, lat, long):
        x_pos = int(np.ceil((long-ymin) /  length))
        y_pos = int(np.ceil((lat-xmin) / width))
        return x_pos, y_pos

    def c_plot(self):
        shp_attributes.clear()
        random_col()
        self.ui.figure.clear()
        ax = self.ui.figure.add_subplot(111)
        ax.axis('off')
        print(list_of_shp_files)
        print(list_of_shp_files[:-1])
        try:
            for i in range(len(list_of_shp_files)):
                # print(i)
                self.f_name = list_of_shp_files[i]
                # print(self.f_name)
                self.shape_file = gpd.read_file(self.f_name)
                # print(list_of_shp_files)
                # print(self.shape_file.STATE_N)
                # self.yaga= list()


                # PROCESSING FOR ATTRIBUTE
                prop_keys_list = []
                prop_attr_list = []
                # RUNNING BOTH LOOPS PARALLEL
                

                # for i in range(1000):
                #     prop_attr_list.append(i)
                #     prop_keys_list.append(i)

                shp_attributes.append(self.shape_file)
                # print(shp_attributes.geometry)
                # print(self.yaga)
                # shp_attributes.append(self.yaga)
                # print(self.shape_file)
                # print(self.yaga)
                # CHECK IF THE PROJECT OF THE SHAPEFILE IS SAME OR NOT AND THEN SET IT ACCORDINGLY

                if self.shape_file.crs['init'] != 'epsg:32644':
                    print("work")
                    # print(self.shape_file.private variables in pythoncrs['init'])
                    self.data_proj = self.shape_file.copy()
                    self.data_proj['geometry'] = self.data_proj['geometry'].to_crs(epsg=32644)
                else:
                    print("work")
                    self.data_proj = self.shape_file.copy()
                # print(self.f_name)
                if(self.f_name == './grid.shp'):
                    print("grid plot")
                    self.data_proj .plot(categorical=True,
                               ax=ax,
                               legend=True,
                               facecolor="none",
                               edgecolor='black',
                               figsize=(60, 60),
                               markersize=45
                              )
                else:
                    self.data_proj .plot(categorical=True,
                               ax=ax,
                               color=color_list[i],
                               legend=True,
                               edgecolor='black',
                               figsize=(60, 60),
                               markersize=45
                              )

                if(self.data_proj['geometry'][0].type == 'Point'):
                    self.data_proj.apply(lambda x: ax.annotate(s='P ' + x.Name, xy=x.geometry.centroid.coords[0], 
                        ha='center', va='bottom', weight='bold'),axis=1)
                    print(self.data_proj.Name)
                    # # print("ewsedrtfygvhbjbh")
                    # for idx, row in c.iterrows():
                    #     print(row)
                    #     self.data_proj.annotate(s='P' + (idx + 1), xy=row.geometry.centroid.coords[0],
                    #                 horizontalalignment='center')


                for feat in fiona.open(self.f_name):
                    prop_keys_list = feat.keys()

                for i in prop_keys_list:
                    for feat in fiona.open(self.f_name):
                        prop_attr_list.append(feat[i])
                
                for i, j in zip(prop_keys_list, prop_attr_list):
                    print(i,j)
        except:
            #print("ERROR!!!")
            del list_of_shp_files[-1]
        print("is it working")
        print(xmin,ymin,xmax,ymax)
        self.ui.canvas.draw()

    def get_path_with_grid(self):
        print(type(self.cd.startCell.text()))
        print(self.cd.endCell.text())
        self.start = self.cd.startCell.text()
        print(type(self.start))
        self.end = self.cd.endCell.text()

        print("WORKING")
        print(self.__text)
        try:
            self.cd.view1.clear()
            self.path = 'beat' + str(self.__text) + '.png'
            print(self.path)
            self.beat_path = PathGeneration(self.path)
            self.beat_path.add_grid()
            self.beat_path.cal_path(int(self.start), int(self.end))
            self.beat_path.draw_path()
            self.cd.show()
            pixmap= QPixmap('./newGrid.png')
            grap= QtWidgets.QGraphicsPixmapItem(pixmap)
            self.cd.view1.addItem(grap)
            self.cd.canvas1.show()
        except Exception as e:
            print(e)
            print("Error")
            ok = QMessageBox.about(self, ' ', "File not iterable")

    def showCellDialog(self):
        
        try:
            self.cd.view1.clear()
            self.path = 'beat' + str(self.__text) + '.png'
            print(self.path)
            self.beat_path = PathGeneration(self.path)
            self.beat_path.add_grid()
            # self.beat_path.cal_path(204, 487)
            self.beat_path.draw_path_no_grid()
            self.cd.show()
            pixmap= QPixmap('./Grid.png')
            grap= QtWidgets.QGraphicsPixmapItem(pixmap)
            self.cd.view1.addItem(grap)
            self.cd.canvas1.show()
        except:
            print("Error")
            ok = QMessageBox.about(self, ' ', "File not iterable")

               

    def getFile(self):
            
            try:
                #self.fname = ""
                self.fname = QFileDialog.getOpenFileName(self,'Open File','D:\Work\Basemaps\Basemaps', "Shape Files (*.shp) ;; Image Files (*.png,*.jpg)")
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
                print(sys.exc_info()[0], "Exception Caught 1")



    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

 
    

    def dropEvent(self, event):
           
            # self.fname = QtCore.QUrl.fileName(event.mimeData().urls())
            for url in event.mimeData().urls(): 
                list_of_shp_files.append(url.toLocalFile())
            self.c_plot()
            self.get_table()
            

            
                        
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

            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(list_of_shp_files)
           

    def showDialog(self):
            
            self.__text, ok = QInputDialog.getText(self, 'Enter Beat Region', 
                'Beat Region Number:')
    
            if ok:
                self.showChooseDialog()
                

    def showChooseDialog(self):
            self.pd.show()            

    
            


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = MyForm()
    mainwin.show()
    sys.exit(app.exec_())