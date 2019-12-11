import shapely
from shapely.ops import cascaded_union
import json
import geojson
from matplotlib import pyplot as plt
import geopandas as gpd

with open('D:/Work/PatrolGIS/PatrolGis/PyTemp/demo.json') as geojson1:
    poly1_geojson = json.load(geojson1)

with open('D:/Work/PatrolGIS/PatrolGis/PyTemp/demo1.json') as geojson2:
    poly2_geojson = json.load(geojson2)

print(type(poly1_geojson))
poly1 = shapely.geometry.asShape(poly1_geojson['features'][2]['geometry'])
poly2 = shapely.geometry.asShape(poly2_geojson['features'][2]['geometry'])


print(poly1)
print(poly2)
mergedPolygon = poly1.union(poly2)

geojson_out = geojson.Feature(geometry=mergedPolygon, properties={})

with open('Merged_Polygon.json', 'w') as outfile:
    json.dump(geojson_out.geometry, outfile, indent=3)
outfile.close()