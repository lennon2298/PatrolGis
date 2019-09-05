# from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import geopandas as gpd

# test = gpd.read_file('../shapefiles/BEAT.shp')
# # test = GeoDataFrame.from_file('../shapefiles/BEAT.shp')
# # test.set_index('id', inplace=True)
# # test.sort()

# # CALC AREA 
# test['area'] = test['geometry'].area/ 10**6
# print(test['geometry'])
# BLUE = '#6699cc'
# print(len(test['geometry']))
# for i in range(0, len(test['geometry'])):
#     # GET GEOMETRY AND AREA OF SPECIFIC BEAT
#     poly= test['geometry'][i]
#     area = test["area"][i]
    
#     fig = plt.figure()
#     ax = plt.gca()
#     plt.gca().axes.get_yaxis().set_visible(False)
#     plt.gca().axes.get_xaxis().set_visible(False)
#     # ax=fig.add_subplot(111)
#     ax.add_patch(PolygonPatch(poly, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2 ))
#     ax.axis('scaled')

#     # Remove whitespace from around the image
#     fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
#     f_name = 'beat' + str(i)
#     ''' SAVE TO TEXT FILE '''
#     file_name = f_name + ".txt"
#     f = open(file_name, "w+")
#     f.write(str(area))
#     f.close()

#     # SAVE IMAGE
#     plt.savefig(f_name, bbox_inches='tight', pad_inches = 0)
#     plt.close()

class SplitBeatFile():

    self.__BLUE = '#6699cc'

    def __init__(self, f_name):
        self.f_name = f_name
        self.f_name = gpd.read_file(self.f_name)
    
    def cal_area(self):
        if self.f_name is not None:
            test['area'] = test['geometry'].area/ 10**6

    def split(self):
        for i in range(0, len(test['geometry'])):
            # GET GEOMETRY AND AREA OF SPECIFIC BEAT
            poly= test['geometry'][i]
            area = test["area"][i]
            
            fig = plt.figure()
            ax = plt.gca()
            plt.gca().axes.get_yaxis().set_visible(False)
            plt.gca().axes.get_xaxis().set_visible(False)
            # ax=fig.add_subplot(111)
            ax.add_patch(PolygonPatch(poly, fc=self.__BLUE, ec=self.__BLUE, alpha=0.5, zorder=2 ))
            ax.axis('scaled')

            # Remove whitespace from around the image
            fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
            self.temp_f_name = 'beat' + str(i)
            ''' SAVE TO TEXT FILE '''
            self.file_name = self.temp_f_name + ".txt"
            self.f = open(file_name, "w+")
            self.f.write(str(area))
            self.f.close()

            # SAVE IMAGE
            plt.savefig(self.temp_f_name, bbox_inches='tight', pad_inches = 0)
            plt.close()