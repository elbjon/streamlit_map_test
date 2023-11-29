import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static


# Create a map using the Map() function and the coordinates for Boulder, CO
#m = folium.Map(location=[52.8, 10.8], tiles="cartodb positron")

# Display the map
#m









f = folium.Figure(width=1000, height=500)
m = folium.Map(location= [52, 10], 
           tiles="openstreetmap",
           zoom_start=10, 
           min_zoom = 6,
           max_bounds = True 
           ).add_to(f)







# center on Liberty Bell, add marker
x = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="HELLO", tooltip="HELLOHELLO"
).add_to(x)

# call to render Folium map in Streamlit
folium_static(x)
#st_folium(m, width=725)
