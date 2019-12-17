import geopandas as gpd
import shapely

poly = gpd.read_file('../shapefiles/BEAT.shp')

points = gpd.read_file('../shapefiles/Wireless_station.shp')
poly['geometry'] = poly['geometry'].to_crs(epsg=4326)
# joinDF=gpd.sjoin(points, poly, how='left',op="within")

# print(joinDF)
# print(poly.total_bounds)
# polygon = poly['geometry'][3]
for i in range(0, len(poly['geometry'])):
    if poly['BEAT_N'][i] == 'BHAGPOR':
        polygon = poly['geometry'][i]  
new_polygon = shapely.geometry.asShape(polygon)
print(new_polygon.bounds)