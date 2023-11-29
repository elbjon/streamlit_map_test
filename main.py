import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static
import os



def get_pos(lat, lng):
    return lat, lng


m = folium.Map()

m.add_child(folium.LatLngPopup())

map = st_folium(m, height=350, width=700)

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

if data is not None:
    st.write(data) # Writes to the app
    print(data) # Writes to terminal





f = folium.Figure(width=1000, height=500)
m = folium.Map(location= [52, 10], 
           tiles="openstreetmap",
           zoom_start=10, 
           min_zoom = 6,
           max_bounds = True 
           ).add_to(f)


folium_static(f)




# center on Liberty Bell, add marker
x = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="HELLO", tooltip="HELLOHELLO"
).add_to(x)

# call to render Folium map in Streamlit
folium_static(x)
#st_folium(m, width=725)


st.write('Here we go:')

m = folium.Map(tiles=None)
folium.TileLayer("OpenStreetMap").add_to(m)
folium.TileLayer("cartodb positron",show=False).add_to(m)
folium.TileLayer(
            tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr = 'Esri',
            name = 'Esri Satellite',
            show=False,
            overlay = False,
            control = True
           ).add_to(m)

folium.TileLayer(
    tiles = 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
    attr='opentopomap.org',
    show=False,
    ).add_to(m)
folium.LayerControl().add_to(m)

folium_static(m)






m = folium.Map([37, 0], zoom_start=1)
merc = '1.png' #= os.path.join("data", "Mercator_projection_SW.png")


if not os.path.isfile(merc):
    print(f"Could not find {merc}")
else:
    img = folium.raster_layers.ImageOverlay(
        name="Mercator projection SW",
        image=merc,
        bounds=[[51.95, 9.97], [53.2, 11.1]],
        opacity=0.6,
        interactive=True,
        cross_origin=False,
        zindex=1,
    )

    folium.Popup("I am an image").add_to(img)

    img.add_to(m)
    folium.LayerControl().add_to(m)




#folium.LayerControl().add_to(m)
#folium.Popup("I am an image").add_to(img)



folium_static(m)
