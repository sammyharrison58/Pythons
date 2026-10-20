import folium
import numpy as np

m = folium.Map(location=[0, 0], zoom_start=2, tiles='CartoDB dark_matter')
for _ in range(400):
    lat = np.random.uniform(-70, 70)
    lon = np.random.uniform(-180, 180)
    folium.CircleMarker(
        location=[lat, lon],
        radius=2,
        color='cyan',
        fill=True,
        fill_opacity=0.7
        
    ).add_to(m)