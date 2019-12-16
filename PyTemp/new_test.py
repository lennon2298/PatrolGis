from gis.algo import *

grid = np.array(board)

# start point and goal
start = (30,71)
goal = (0,0)

print(len(board))
print(len(board[0]))
board = [1]*2000 + 4363*[0]
random.shuffle(board)
board = [board[i:i+7] for i in range(0, 100, 10)]
print(board)
route = astar(grid, start, goal)
route = route + [start]
route = route[::-1]
print(route)


##############################################################################
# plot the path
##############################################################################

 

#extract x and y coordinates from route list
x_coords = []
y_coords = []

for i in (range(0,len(route))):
    x = route[i][0]
    y = route[i][1]
    x_coords.append(x)
    y_coords.append(y)

# plot map and path
fig, ax = plt.subplots(figsize=(20,20))
ax.imshow(grid, cmap=plt.cm.Dark2)
ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)
ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 200)
ax.plot(y_coords,x_coords, color = "black")
plt.show()