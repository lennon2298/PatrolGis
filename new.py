import geopandas as gpd
import matplotlib.pyplot as plt
import os
import earthpy as et



#import shapefile using geopandas

state_poly = gpd.read_file('./shapefiles/STATE.shp')
boundary_poly = gpd.read_file('./shapefiles/BOUNDARY.shp')
beat_poly = gpd.read_file('./shapefiles/BEAT.shp')
forest_poly = gpd.read_file('./shapefiles/DIVISION.shp')
#print(state_poly.head(117))
#print(len(state_poly.head()))
# print(state_poly)
#print(type(state_poly))
#crs type
#print(state_poly.crs)

#total bound
#print(state_poly.total_bounds)
#print(len(state_poly.total_bounds))
#[print(x) for x in state_poly.total_bounds]

# geometry point all 118 points
#print(state_poly.geom_type)

#no of features
#print(state_poly.shape)
# fig, ax = plt.subplots(1,1)

ax = state_poly.plot()
# state_poly.plot(ax=ax)


boundary_poly.plot(axes=ax, color="green")
beat_poly.plot(axes=ax, color="purple")
forest_poly.plot(axes=ax, color="coral")

# ax.set_title("Shape File added")
# ax.set_axis_off()
plt.axis("equal")
plt.show()