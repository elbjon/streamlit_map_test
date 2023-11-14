import streamlit as st
import folium
from streamlit_folium import st_folium


# Create a map using the Map() function and the coordinates for Boulder, CO
#m = folium.Map(location=[52.8, 10.8], tiles="cartodb positron")

# Display the map
#m

















# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="HELLO", tooltip="HELLOHELLO"
).add_to(m)

# call to render Folium map in Streamlit

try:
    st_data = st_folium(m, width=725)
except:
    m
