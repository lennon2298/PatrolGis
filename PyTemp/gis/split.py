# from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import geopandas as gpd


class SplitBeatFile():

    __BLUE = '#6699cc'

    def __init__(self, f_name):
        self.f_name = f_name
        self.f_name = gpd.read_file(self.f_name)
    
    def cal_area(self):
        if self.f_name is not None:
            self.f_name['area'] = self.f_name['geometry'].area/ 10**6

    def split(self):
        for i in range(0, len(self.f_name['geometry'])):
            # GET GEOMETRY AND AREA OF SPECIFIC BEAT
            poly= self.f_name['geometry'][i]
            area = self.f_name["area"][i]
            
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
            self.f = open(self.file_name, "w+")
            self.f.write(str(area))
            self.f.close()

            # SAVE IMAGE
            plt.savefig(self.temp_f_name, bbox_inches='tight', pad_inches = 0)
            plt.close()