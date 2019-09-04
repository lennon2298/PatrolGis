import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from PIL import Image
import matplotlib.path as mplPath
import numpy as np
import math
# Open image file
image = Image.open('.\\beat25.png')
my_dpi=54
# print(type(image))
pix = image.load()
# Set up figure
fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
ax=fig.add_subplot(111)
plt.axis('auto')
ax.grid(which='major', axis='both', linestyle='-', color='r')
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

# print(points_list[0][2])
print(nx, ny)
count = 0
count_zero = 0

# Add some labels to the gridsquares
for j in range(ny):
    y=myInterval/2+j*myInterval
    for i in range(nx):
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
        count = count + 1
        # print(pix[x,y][0], pix[x,y][1], pix[x,y][2])
        # plt.plot(x, y, 'ro')

# Save the figure
x = 331
asd = int((count + 1)/nx)*myInterval
print(asd)
x1 = (myInterval/2.+int(x%nx)*myInterval)
y1 = (myInterval/2.+math.floor(x/nx)*myInterval)
xx = 997
print(int(xx/nx))
x2 = (myInterval/2.+int(xx%nx)*myInterval)
y2 = (myInterval/2.+math.floor(xx/nx)*myInterval)
print(x1, x2)
print(y1, y2)
t = [x1, x2]
s = [y1, y2]
print(points_list)
print(count_zero)
plt.plot(t, s, linewidth = 1, color='k')
# ax.grid(False)
fig.savefig('myImageGrid1')