# LIST OF GLOBAL VARIABLES

import randomcolor
import numpy as np


# LIST OF ALL THE SHAPEFILES
list_of_shp_files = list()

# LIST OF ATTRIBUTES OF SHAPE FILES
shp_attributes = list ()

route_points = list()
grid_mat = []
new = []
# grid_mat = np.ones((700,700), dtype=int)
for i in range(150):
    for j in range(150):
        new.append(1)
    grid_mat.append(new)
    new = []


xmin,ymin,xmax,ymax = 0, 0, 0, 0
length = 0.0025
width = 0.0025
rows = 0
cols = 0

# LIST OF EDGECOLORS
color_list = list()

# function to generate random color


def random_col():
    rand_color = randomcolor.RandomColor()
    main_color = rand_color.generate()

    if main_color in color_list:
        rand_color()
    else:
        color_list.append(main_color[0])
    return True