import folium
import geopy
import pandas
from geopy.geocoders import ArcGIS
l=ArcGIS()
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name=list(data["NAME"])
def icon_color(elevation):
    if el < 1500:
        return "green"
    elif 1500 <= el <2000:
        return "orange"
    else:
        return "red"
html="""Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m"""
map=folium.Map(location=[38.88,-99.1],zoom_start=6,tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="Volcanoes")

for la,lo,el ,name in zip(lat,lon,elev,name):
    iframe=folium.IFrame(html=html % (name,name,el),width=200,height=100)
    fgv.add_child(folium.CircleMarker(radius=10,location=[la,lo],popup=folium.Popup(iframe),color="black",fill=True,fill_color=icon_color(el),fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json" , "r", encoding = "utf-8-sig").read(),style_function=lambda x :
{ 'fillColor':"yellow" if x["properties"]["POP2005"] < 1500000 else "orange" if 1500000 <= x["properties"]["POP2005"] < 2000000 else "red"}))

#folium.LatLngPopup().add_to(map)
map.add_child(fgp)
map.add_child(fgv)
folium.LatLngPopup().add_to(map)
map.add_child(folium.LayerControl())
map.save("Map1.html")
