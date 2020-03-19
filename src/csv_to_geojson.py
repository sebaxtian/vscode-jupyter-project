# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # CSV to GeoJSON
# This is an example to show how we can use pandas and geopandas to transform CSV file to GeoJSON file

# %%
# Import modules
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os


# %%
# Constants
INPUT_DIR = "../input"
OUTPUT_DIR = "../output"


# %%
# Load dataset into dataframe
dataframe = pd.read_csv(os.path.join(INPUT_DIR, 'crash_data.csv'))
dataframe.shape


# %%
# Show dataframe
dataframe.head()


# %%
# Create a geodataframe from dataframe
geodataframe = gpd.GeoDataFrame(dataframe, geometry=gpd.points_from_xy(dataframe.lng, dataframe.lat))
geodataframe.shape


# %%
# Show geodataframe
geodataframe.head()


# %%
# Plot the coordinates over a country-level map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# We restrict to United States of America
ax = world[world.name == 'United States of America'].plot(
    color='white', edgecolor='black')

# We can now plot our GeoDataFrame
geodataframe.plot(ax=ax, color='red')

# Save PNG image
plt.savefig(os.path.join(OUTPUT_DIR, 'crash_data.png'))

# Plot GeoDataFrame
plt.show()


# %%
# Save GeoJSON from GeoDataFrame
geodataframe.to_file(os.path.join(OUTPUT_DIR, 'crash_data.geojson'), driver='GeoJSON')


# %%


