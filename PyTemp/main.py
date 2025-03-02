from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication, QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem, QListWidgetItem, QListWidget, QInputDialog, QAbstractItemView, QMessageBox, QFileSystemModel, QTreeView)
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QPixmap
from resource_rc import *
import sys
from newUI import Ui_MainWindow
from cellDialog import Ui_cellDialog
from cellDia2 import Ui_cellDialog2
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
from gis.pos import *
import numpy as np
import fiona
import heapq
import matplotlib.image as mpimg
import os.path
from shapely.geometry import Polygon
from shapely.geometry import Point
import shapely
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
        self.ui.menuCreatePath.triggered.connect(self.showChooseDialog)
        # self.ui.menuSplit.triggered.connect(self.create_grid)
        self.setAcceptDrops(True)
        # self.setDragDropMode(QAbstractItemView.InternalMove)
        # self.ui.setAcceptDrops(True)
        self.ui.frame_3.setAcceptDrops(True)
        self.cd = Ui_cellDialog(self)
        self.cd2 = Ui_cellDialog2(self)
        self.pd = Ui_Dialog(self)
        # print(self.cd.startCell.text())
        # print(self.cd.endCell.text())
        self.cd.okButtonCd.clicked.connect(self.get_position)
        self.cd.cancelButtonCd.clicked.connect(self.cd.close)
        self.pd.pushButton.clicked.connect(self.showCellDialog)
        self.pd.pushButton_2.clicked.connect(self.showCellDialog2)
        
        # self.ui.setDragDropMode(QAbstractItemView.InternalMove)


    def get_position(self):
        pos1 = self.cd.startCell.text()
        pos2 = self.cd.endCell.text()
        print(pos1, pos2)
        arr_pos1 = get_coordinates(pos1)
        if arr_pos1 is None:
            raise ValueError("Enter a legit start position")
        arr_pos2 = get_coordinates(pos2)
        if arr_pos2 is None:
            raise ValueError("Enter a legit start position")
        print(arr_pos1)
        print(arr_pos2)
        self.create_grid(get_dercs(pos1))
        start = self.get_cell(arr_pos1[0], arr_pos1[1])
        goal = self.get_cell(arr_pos2[0], arr_pos2[1])
        # print(start)
        # print(goal)

        # PROCESS FOR GET DATA FROM out2.json and and calulate the path
        print("calculating path")
        # start = (30,71)
        # goal = (0,0)
        global board
        grid = np.array(board)
        board = [1]*4363 + 2000*[0]
        random.shuffle(board)
        board = [board[i:i+7] for i in range(0, 100, 10)]
        print(board)
        route = astar(grid, start, goal)
        route = route + [start]
        route = route[::-1]
        print(route)
        self.get_coords(route)
        self.cd.close()
        return True

    def get_coords(self, route):
        pnt_coords = []
        mid_pnt = length / 2
        for row in route:
            for j in range(2):
                # print(row[j], end = " ")
                if(j == 0):
                    row_coords = (ymax - mid_pnt) - row[j]*length
                    print(row_coords, end = ' ')
                    pnt_coords.append(row_coords)
                elif(j == 1):
                    row_coords = (xmin + mid_pnt) + row[j]*length
                    print(row_coords)
                    pnt_coords.append(row_coords)
                # new = 
            route_points.append(list(reversed(pnt_coords)))
            pnt_coords = []
        self.create_line_shp()
            # print()
        

    def create_line_shp(self):
        # print(route_points)
        # line_string = Point(route_points)
        line_string = []
        for row in route_points:
            # print(row)
            line_string.append(Point(row))
        path = gpd.GeoDataFrame({'geometry':line_string})
        path.crs = {'init' :'epsg:4326'}
        path.to_file('./path.shp')
        list_of_shp_files.append('./path.shp')
        self.c_plot()
        self.get_table()

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

    def create_grid(self, descr):
        # point_shp = gpd.read_file('../shapefiles/Wireless_station.shp')
        # print(f_name)
        print(descr)
        polygon_shp = gpd.read_file('../shapefiles/BEAT.shp')
        polygon_shp['geometry'] = polygon_shp['geometry'].to_crs(epsg=4326)
        # print(poly['geometry'][0].coords.xy)
        # print(poly.geometry.centroid.coords[0].x)
        for i in range(0, len(polygon_shp['geometry'])):
            if polygon_shp['BEAT_N'][i] == descr:
                polygon = polygon_shp['geometry'][i]  
        poly = shapely.geometry.asShape(polygon)
        global xmin,ymin,xmax,ymax, rows, cols
        xmin,ymin,xmax,ymax = poly.bounds
        print(xmin,ymin,xmax,ymax,length,width)
        rows = int(np.ceil((ymax-ymin) /  length))
        cols = int(np.ceil((xmax-xmin) / width))
        print(rows, cols)
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
        f_data = open("new_data.txt", "w+")
        
        f_data.write(str(grid_mat))
        f_data.close()

        grid = gpd.GeoDataFrame({'geometry':polygons})
        # grid.to_file('grid.shp')
        # grid['geometry'] = grid['geometry'].to_crs(epsg=32644)
        grid.crs = {'init' :'epsg:4326'}
        grid.to_file('./grid.shp')
        print("here")
        # print(self.get_cell(80.6174166666667, 22.3383333333333))
        # print(grid)
        list_of_shp_files.append('./grid.shp')
        self.c_plot()
        self.get_table()
        # list_of_shp_files.append('./grid.shp')
        # self.c_plot()
        # self.get_table()
        ok = QMessageBox.about(self, ' ', "Process Started")


    def get_cell(self, g_lat, g_long):
        print(g_long, ymin)
        x_pos = int(np.ceil((g_long-ymin) /  length))
        y_pos = int(np.ceil((g_lat-xmin) / width))
        print(y_pos)
        print(x_pos)
        return (rows - x_pos), y_pos
    
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
                # print("lolol " + self.data_proj['geometry'][0].type)
                if(self.data_proj['geometry'][0].type == 'Point'):
                    print(self.data_proj['geometry'][0])
                    self.data_proj.apply(lambda x: ax.annotate(s='P ' + x.Name, xy=x.geometry.centroid.coords[0], 
                        ha='center', va='bottom', weight='bold'),axis=1)
                    # print(self.data_proj.geometry.centroid.x.iloc[0])
                    self.geojson_file = gpd.read_file(self.f_name)
                    self.geojson_file.to_file('./out2.json', driver='GeoJSON')
                    # print(self.data_proj.Name)
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
            self.cd.show()
            
        except:
            print("Error")
            ok = QMessageBox.about(self, ' ', "File not iterable")

    
    def showCellDialog2(self):
        {
            self.cd2.show()   
        }

               

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