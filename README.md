# Part 1: Set Up

## starchart.py

This script connects to the skyfield api. Skyfield computes positions for the stars, planets, and satellites in orbit around the Earth. Its results should agree with the positions generated by the United States Naval Observatory and their Astronomical Almanac to within 0.0005 arcseconds (half a “mas” or milliarcsecond).

This code is loading a catalog of stars from the Hipparcos satellite, and then converting the celestial coordinates of the stars (right ascension and declination) and their parallax (distance from Earth) into Cartesian coordinates.

The code first uses the skyfield.api.load and skyfield.data.hipparcos libraries to load the Hipparcos catalog data into a Pandas DataFrame, and then extracts the right ascension, declination, and parallax values from the DataFrame.

The parallax values are then used to convert the celestial coordinates into Cartesian coordinates using the following formulas:
x = parallax * cos(dec) * cos(ra)
y = parallax * cos(dec) * sin(ra)
z = parallax * sin(dec)

Next, the code finds all the points that do not have NaN values, and then writes the valid coordinate data to a file named coordinates.py using the open('coordinates.py', 'w') function. This is done by iterating through the valid indices, and writing each set of x, y, and z coordinates as a list in a string format to the file.

# Part 2: Spatial Partitioning System

Spatial partitioning is a technique used to divide a large 3D environment into smaller regions, in order to reduce the number of objects that need to be rendered at any given time. In this section, we will take the data obtained from the previous section and 

## sortcoords.py

This script imports the list of coordinates from the file created in starchart.py. It then uses the coordinates data to create an R-tree index, which is a data structure used for efficient spatial searching. The index is created with the rtree library, and the index.Property() and index.Index() functions are used to set the properties of the index. In this case, the dimension is set to 3, indicating that the index will be used for 3-dimensional spatial data.

The code then defines a function distanceFromOrigin(point) that calculates the distance of a point from the origin in 3D space. This function is then used as a sort key when inserting items into the R-tree, so that the items are stored in the tree sorted by their distance from the origin.

The console output:
rtree.index.Index(bounds=[-307.87948664160047, -547.1638629074088, -686.1904208849583, 244.52676297236007, 356.16450904206494, 245.42405136439612], size=117955)

This is the default string representation of the rtree.index.Index object, which displays some information about the R-tree index, including the bounds of the index and the number of items stored in the tree.

The bounds of the index are represented by the first six values in square brackets. They are the minimum and maximum values of x, y and z coordinates of the points stored in the R-tree. The size of the index is represented by the value after the comma, which is the number of items stored in the tree.

# Part 3: Adding a Playable Character

the location of this character needs to be constantly checked against the spatial partitioning system so that we only implement the partition that the player is currently located inside of at any given time

# Part 4: Frontend

## index.html

## style.css

## main.js

# Part 5: Putting it all together