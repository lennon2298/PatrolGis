import json
import geojson
import geopandas as gpd

class SaveToGeoJSON:
    __name_counter = 0

    def file_name(self):
        if self.__name_counter == 0:
            self.__name_counter = 1
            return "./out"+str(self.__name_counter)+".json"
        elif self.__name_counter == 1:
            self.__name_counter = 2
            return "./out"+str(self.__name_counter)+".json"
        else:
            self.__name_counter = 0
            print("Contact developer")

    def save(self, name, file_save_name):
        self.shape_file = gpd.read_file(name)
        self.shape_file.to_file(file_save_name, driver="GeoJSON")

class MergeGeoJSON:
    __files_merge_list = ['./out1.json', './out2.json']
    __poly_geojson = list()
    def save(self):
        for i in self.__files_merge_list:
            with open(i) as geojson_data:
                self.__poly_geojson.append(json.load(geojson_data))
        merged = { 'firstObj ' : self.__poly_geojson[1], 'secondObj' : self.__poly_geojson[0] }
        json.dumps(merged)

        with open('Merged_out.json', 'w') as outfile:
            json.dump(merged, outfile, indent=3)
        outfile.close()
        
        return True
        