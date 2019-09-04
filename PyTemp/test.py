import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from PIL import Image
import matplotlib.path as mplPath
import numpy as np
import collections 
import math
# Open image file
image = Image.open('./beat25.png')

# Open image file
image = Image.open('.\\beat25.png')
my_dpi=54
# print(type(image))
pix = image.load()
# Set up figure
fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
ax=fig.add_subplot(111)
plt.axis('auto')
ax.grid(which='major', axis='both', linestyle='-', linewidth=1, color='r')
# Remove whitespace from around the image
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

# Set the gridding interval: here we use the major tick interval
myInterval=16
loc = plticker.MultipleLocator(base=myInterval)
loc1 = plticker.MultipleLocator(base=myInterval)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc1)

# Add the grid


# Add the image
ax.imshow(image)

# Find number of gridsquares in x and y direction
nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval)))
ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval)))

points_list = np.empty((ny, nx))
points_list = points_list.astype(int)
# print(points_list[0][2])
print(nx, ny)
count = 0
count_zero = 0

# REVERSE POINT LIST
reverse_point_list = dict()

# Add some labels to the gridsquares
for j in range(ny):
    y=myInterval/2+j*myInterval
    for i in range(nx):
        temp_loc_list = list()
        x=myInterval/2.+float(i)*myInterval
        # pnt = [int(x),int(y)]
        # print(x, y)
        r=0.001
        if(pix[x,y][0] < 255):
            points_list[j][i] = 0
            count_zero += 1
        else:
            # print(i, j)
            points_list[j][i] = -1
        ax.text(x,y,count,color='g',ha='center',va='center')
        
        # REVERSE LIST GRID VALUE TO STORED VALUE
        temp_loc_list.append(j)
        temp_loc_list.append(i)
        reverse_point_list[count] = {
            "val": points_list[j][i],
            "loc": temp_loc_list
        }
        count = count + 1
        # print(pix[x,y][0], pix[x,y][1], pix[x,y][2])
        # plt.plot(x, y, 'ro')

# Save the figure
# print(points_list)
# print(count_zero)
# print(reverse_point_list)

def print_data():
    for i in range(0,len(points_list)):
        for j in range(0,len(points_list[i])):
            print(points_list[i][j], end=" ")
        print("\n")

def area_check(pos):
    if reverse_point_list[pos]['val'] == 0:
        return True
    else:
        return False

print(area_check(412))

def bfs(grid, start, goal):
    
    if len(points_list) != 0:
        width = len(points_list[0])
        height = len(points_list)
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
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != 1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
            if x2 == r_x and y2 == r_y:
                return path
        
                
copy_point_list = points_list

def cal_path(start_pos, end_pos):
    start_list = [i for i in reverse_point_list[start_pos]['loc']]
    end_list = [i for i in reverse_point_list[end_pos]['loc']]
    x_start, y_start = [i for i in reverse_point_list[start_pos]['loc']]
    x_end, y_end = [i for i in reverse_point_list[end_pos]['loc']]
    # print(x_start, " ", y_start)
    # print(x_end, " ", y_end)
    start_list = frozenset(start_list)
    end_list = frozenset(end_list)
    path = bfs(points_list, start_list, end_list)
    for i in path:
        # print(i)
        x, y = [z for z in i]
        # print(x," ",y)
        copy_point_list[x][y] = 1
    return True
        
    # print(path)


def reverse_print_data():
    for i in range(0,len(copy_point_list)):
        for j in range(0,len(copy_point_list[i])):
            print(copy_point_list[i][j], end=" ")
        print("\n")

# print_data()
cal_path(412, 700)
reverse_print_data()
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

x_list = []
y_list = []

for j in range(ny):
    y=myInterval/2+j*myInterval
    for i in range(nx):
        x=myInterval/2.+float(i)*myInterval
        if(copy_point_list[j][i] == 1):
            x_list.append(x)
            y_list.append(y)
        

# print(points_list)
# print(count_zero)
plt.plot(x_list, y_list, linewidth = 1, color='k')
# ax.grid(False)
fig.savefig('myImageGrid1')