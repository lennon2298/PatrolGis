import geopandas as gpd

shape_file = gpd.read_file("/home/bot/Work/GIS/PatrolGis/shapefiles/BEAT.shp")
# if shape_file.crs['init'] != 'epsg:32644':
#     print("work")
#     # print(self.shape_file.private variables in pythoncrs['init'])
#     data_proj = shape_file.copy()
#     shape_file['geometry'] = data_proj['geometry'].to_crs(epsg=32644)
#     print(shape_file.crs['init'])
#     # print(shape_file['geometry'])
shape_file.to_file('./out2.json', driver='GeoJSON')