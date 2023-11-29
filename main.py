import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static
#from folium.plugins import ImageOverlay
#from folium.plugins import ImageOverlay
from io import BytesIO
from PIL import Image


# Create a map using the Map() function and the coordinates for Boulder, CO
#m = folium.Map(location=[52.8, 10.8], tiles="cartodb positron")

# Display the map
#m


 
from streamlit_folium import st_folium



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





# Create a Folium map centered at a specific location
m = folium.Map(location=[52, 10], zoom_start=10)

# Load your image
image_path = "1.png"
img = Image.open(image_path)

# Convert the image to BytesIO object
img_byte_array = BytesIO()
img.save(img_byte_array, format='PNG')

# Create an ImageOverlay
image_overlay = ImageOverlay(
    img_byte_array.getvalue(),
    bounds=[[52, 10], [53, 11]],
    opacity=0.6,
)

# Add the ImageOverlay to the Folium map
image_overlay.add_to(m)

# Display the map in Streamlit
st.markdown(m._repr_html_(), unsafe_allow_html=True)



#folium.LayerControl().add_to(m)
#folium.Popup("I am an image").add_to(img)


img.add_to(m)







folium_static(m)
