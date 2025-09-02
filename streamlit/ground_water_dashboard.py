#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 19:02:31 2025

@author: wagnerapel
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
from warnings import filterwarnings
from streamlit_folium import st_folium
filterwarnings('ignore')

# Disable cache to force rebuild
@st.cache_data(ttl=0)  # ttl=0 disable cache
def load_data():
    return None  

# Configure the Matplotlib backend to be compatible with Streamlit
import matplotlib
matplotlib.use('Agg')  # 'Agg' backend for non-interactive rendering

st.title("Hydrological Monitoring in Queensland")

df = pd.read_csv('../data/processed/groundwater_clean.csv') 

# Start
st.subheader("Table - Basin Name, Formation, Latitude and Longitude")
st.dataframe(df.reset_index(drop=True))


# Plot char bars:
st.subheader("Number of monitoring points per river")
st.write("""
This dashboard visualizes groundwater monitoring points in Queensland, using real data from the Queensland Government (data.qld.gov.au). 
It employs **MarkerCluster** to group points for better readability and is designed to be inclusive, making complex data accessible to 
both professionals and the general public through an interactive map and charts.
""")

# Top 20 - Vertical
fig1, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, x="FORMATION", order=df['FORMATION'].value_counts().nlargest(20).index)
plt.xticks(rotation=90)
ax.set_title("Top 20 Points per River\n")
st.pyplot(fig1)

# Folium
st.subheader("Monitoring Points Map")
st.write("The points are grouped into clusters to facilitate visualization in dense areas. Zoom in to see details.")
map_center = [-27.4698, 153.0251]  # Approximate coordinates of Brisbane
mapa = folium.Map(location=map_center, zoom_start=10)

# Group points into clusters
marker_cluster = MarkerCluster().add_to(mapa)

for i, row in df.iterrows():
    folium.Marker(
        location=[row['LAT'], row['LONG']],
        popup=f"Formation: {row['FORMATION']}",
        icon=folium.Icon(color="blue", icon="tint", prefix="fa")
).add_to(marker_cluster)
    
st_folium(mapa, width=700, height=500)

#footbar
st.markdown('----')
st.markdown("**Note:** The dashboard provides analysis on real data from the website https://www.data.qld.gov.au/dataset")