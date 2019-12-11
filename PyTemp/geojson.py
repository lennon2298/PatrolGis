import geopandas as gpd

shape_file = gpd.read_file("D:/Work/Major/PatrolGIS/shapefiles/BEAT.shp")
if shape_file.crs['init'] != 'epsg:32644':
    print("work")
    # print(self.shape_file.private variables in pythoncrs['init'])
    data_proj = shape_file.copy()
    data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=32644)

shape_file.to_file('./out2.json', driver='GeoJSON')