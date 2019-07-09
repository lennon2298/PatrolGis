# LIST OF GLOBAL VARIABLES

import randomcolor



# LIST OF ALL THE SHAPEFILES
list_of_shp_files = list()

# LIST OF ATTRIBUTES OF SHAPE FILES
shp_attributes = list ()


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