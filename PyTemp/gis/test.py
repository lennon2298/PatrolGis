import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from PIL import Image
import matplotlib.path as mplPath
import numpy as np
import collections 
import math
# Open image file
# image = Image.open('./beat25.png')

class PathGeneration():
    def __init__(self, f_name):
        self.image = f_name
        # print(self.image)
        self.image = Image.open('./' + self.image)
        self.count = 0
        self.count_zero = 0
        self.reverse_point_list = dict()

        self.my_dpi=54
        # print(type(image))
        self.pix = self.image.load()
        # Set up figure
        self.fig=plt.figure(figsize=(float(self.image.size[0])/self.my_dpi,float(self.image.size[1])/self.my_dpi),dpi=self.my_dpi)
        self.ax=self.fig.add_subplot(111)
        print(self.ax)
        plt.axis('auto')
        self.ax.grid(which='major', axis='both', linestyle='-', linewidth=1, color='r')
        # Remove whitespace from around the image
        self.fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

        # Set the gridding interval: here we use the major tick interval
        self.myInterval=16

        self.ax.imshow(self.image)

        # Find number of gridsquares in x and y direction
        self.nx=abs(int(float(self.ax.get_xlim()[1]-self.ax.get_xlim()[0])/float(self.myInterval)))
        self.ny=abs(int(float(self.ax.get_ylim()[1]-self.ax.get_ylim()[0])/float(self.myInterval)))

        self.points_list = np.empty((self.ny, self.nx))
        self.points_list = self.points_list.astype(int)

        self.copy_point_list = self.points_list
        print(self.nx, self.ny)


    # # Open image file
    # image = Image.open('.\\beat25.png')
    def add_grid(self):
        
        loc = plticker.MultipleLocator(base=self.myInterval)
        loc1 = plticker.MultipleLocator(base=self.myInterval)
        self.ax.xaxis.set_major_locator(loc)
        self.ax.yaxis.set_major_locator(loc1)

        # print(points_list[0][2])
        print(self.nx, self.ny)
        # count = 0
        # count_zero = 0

        # REVERSE POINT LIST
        # reverse_point_list = dict()

        # Add some labels to the gridsquares
        for j in range(self.ny):
            y=self.myInterval/2+j*self.myInterval
            for i in range(self.nx):
                temp_loc_list = list()
                x=self.myInterval/2.+float(i)*self.myInterval
                # pnt = [int(x),int(y)]
                # print(x, y)
                r=0.001
                if(self.pix[x,y][0] < 255):
                    self.points_list[j][i] = 0
                    self.count_zero += 1
                else:
                    # print(i, j)
                    self.points_list[j][i] = -1
                self.ax.text(x,y,self.count,color='g',ha='center',va='center')
                
                # REVERSE LIST GRID VALUE TO STORED VALUE
                temp_loc_list.append(j)
                temp_loc_list.append(i)
                self.reverse_point_list[self.count] = {
                    "val": self.points_list[j][i],
                    "loc": temp_loc_list
                }
                self.count = self.count + 1

    def print_data(self):
        for i in range(0,len(self.points_list)):
            for j in range(0,len(self.points_list[i])):
                print(self.points_list[i][j], end=" ")
            print("\n")

    def area_check(self,pos):
        if self.reverse_point_list[pos]['val'] == 0:
            return True
        else:
            return False

    # print(area_check(412))

    def bfs(self, grid, start, goal):
        
        if len(self.points_list) != 0:
            width = len(self.points_list[0])
            height = len(self.points_list)
            # print(width)
            # print(height)

        # print(goal)
        # print(start)
        queue = collections.deque([[start]])
        seen = set([start])
        # print(queue)
        # print(seen)
        r_x, r_y = [x for x in goal]
        # print(r_x, " ", r_y)
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            # print(goal)
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != -1 and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
                if x2 == r_x and y2 == r_y:
                    return path

    def cal_path(self, start_pos, end_pos):
        start_list = [i for i in self.reverse_point_list[start_pos]['loc']]
        end_list = [i for i in self.reverse_point_list[end_pos]['loc']]
        x_start, y_start = [i for i in self.reverse_point_list[start_pos]['loc']]
        x_end, y_end = [i for i in self.reverse_point_list[end_pos]['loc']]
        # print(x_start, " ", y_start)
        # print(x_end, " ", y_end)
        start_list = frozenset(start_list)
        end_list = frozenset(end_list)
        path = self.bfs(self.points_list, start_list, end_list)
        for i in path:
            # print(i)
            x, y = [z for z in i]
            # print(x," ",y)
            self.copy_point_list[x][y] = 1
        return True
            
        # print(path)


    def reverse_print_data(self):
        for i in range(0,len(self.copy_point_list)):
            for j in range(0,len(self.copy_point_list[i])):
                print(self.copy_point_list[i][j], end=" ")
            print("\n")

    # print_data()
    # cal_path(565, 769)
    # reverse_print_data()
    # if area_check(412):
    #     print("calculating path")
    #     cal_path()
    # else:
    #     print("Can not generate path")
    # def find_ymax():
    #     count = 0
    #     for i in range(0,len(points_list)):
    #         for j in range(0,len(points_list[i])):
    #             # print(points_list[i][j])
    #             count += 1
    #             if points_list[i][j] == 0.:
    #                 print("Found")
    #                 return count

    def draw_path_no_grid(self):
        x_list = []
        y_list = []

        for j in range(self.ny):
            y=self.myInterval/2+j*self.myInterval
            for i in range(self.nx):
                x=self.myInterval/2.+float(i)*self.myInterval
                if(self.copy_point_list[j][i] == 1):
                    x_list.append(x)
                    y_list.append(y)
                

        # print(points_list)
        # print(count_zero)
        plt.plot(x_list, y_list, linewidth = 1, color='k')
        # ax.grid(False)
        self.fig.savefig('Grid')

    def draw_path(self):
        x_list = []
        y_list = []

        for j in range(self.ny):
            y=self.myInterval/2+j*self.myInterval
            for i in range(self.nx):
                x=self.myInterval/2.+float(i)*self.myInterval
                if(self.copy_point_list[j][i] == 1):
                    x_list.append(x)
                    y_list.append(y)
                

        # print(points_list)
        # print(count_zero)
        plt.plot(x_list, y_list, linewidth = 1, color='k')
        # ax.grid(False)
        self.fig.savefig('newGrid')


# beat_path = PathGeneration('../beat25.png')
# beat_path.add_grid()
# # beat_path.cal_path(260, 770)
# beat_path.draw_path_no_grid()


# beat_path.add_grid()
# beat_path.cal_path(260, 770)
# beat_path.draw_path()