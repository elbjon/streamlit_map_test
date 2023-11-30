import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static
from folium.plugins import Draw

# Create a Streamlit app
st.title("Draw on Map Example")

# Create a Folium map
m = folium.Map(location=[51.5074, -0.1276], zoom_start=10)

# Add a drawing tool to the map
draw = Draw(export=True)
draw.add_to(m)

# Display the map using Streamlit
st_folium(m)

# Get the drawn features
st.write(draw)