import json
import geojson

with open('./out1.json') as geojson1:
    poly1_geojson = json.load(geojson1)

with open('./out2.json') as geojson2:
    poly2_geojson = json.load(geojson2)

merged = { 'firstObj ' : poly1_geojson, 'secondObj' : poly2_geojson }
json.dumps(merged)

with open('Merged_test_out.json', 'w') as outfile:
    json.dump(merged, outfile, indent=3)
outfile.close()