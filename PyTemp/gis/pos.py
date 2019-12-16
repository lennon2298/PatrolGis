import json

# with open('out2.json') as f:
#     data = json.load(f)

# print(data)
# print("printing features")
# # print(data['features'])
# for i in data['features']:
#     if i['properties']['Name'] == p:
#         return i['geometry']['coordinates']
#     # print(i['properties']['Name'])
# # for feature in data[]

def get_coordinates(position):
    with open('out2.json') as f:
        data = json.load(f)
    
    for i in data['features']:
        if i['properties']['Name'] == position:
            return i['geometry']['coordinates']
        else:
            continue
        return False


# pos1 = get_coordinates("09")
# if pos1 == False:
#     print("Enter a valid position")
# else:
#     print(pos1)