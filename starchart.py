from skyfield.api import Star, load
from skyfield.data import hipparcos
import matplotlib.pyplot as plt
import numpy as np

# Load the Hipparcos catalog data into a Pandas DataFrame
with load.open(hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)

# Extract right ascension and declination
ra = df['ra_degrees'].values # in degrees
dec = df['dec_degrees'].values # in degrees

# Extract parallax
parallax = df['parallax_mas'].values # in arcseconds

# Convert the celestial coordinates and parallax data to Cartesian coordinates
x = parallax * np.cos(np.deg2rad(dec)) * np.cos(np.deg2rad(ra))
y = parallax * np.cos(np.deg2rad(dec)) * np.sin(np.deg2rad(ra))
z = parallax * np.sin(np.deg2rad(dec))

# Find all the points that do not have NaN value
valid_indices = np.where(np.logical_and(np.logical_and(~np.isnan(x), ~np.isnan(y)), ~np.isnan(z)))

# Write the coordinate data to a file (named coordinates.py)
with open('coordinates.py', 'w') as f:
    f.write('const coordinates = [')
    f.write(',\n'.join([f'[{x[i]}, {y[i]}, {z[i]}]' for i in valid_indices[0]]))
    f.write(']\n')

# Optional code that will generate a 3d scatter plot on your local machine
"""
# Create the 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='o')

# Customize the plot
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')
ax.set_title('3D Scatter Plot of Hipparcos Stars')

plt.show()
"""