from rtree import index
from coordinates import coordinates
import math
import pandas as pd

# Create an R-tree
p = index.Property()
p.dimension = 3  # 3-dimensional space
sortedCoords = index.Index(properties=p)

# Define a function to calculate the distance from origin for each point
def distanceFromOrigin(point):
    x, y, z = point
    return math.sqrt(x**2 + y**2 + z**2)

# Insert items into the R-tree, sorted by distance from origin
for i, coord in enumerate(coordinates):
    sortedCoords.insert(i, coord, distanceFromOrigin(coord))

# Now you can use the `sortedCoords` R-tree to perform spatial queries.
print(sortedCoords)