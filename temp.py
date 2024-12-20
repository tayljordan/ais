import json
import folium

# File path for AIS data
file_path = '/Users/jordantaylor/PycharmProjects/ais-data/ais_data.json'

# Load the vessel data from the JSON file
with open(file_path, 'r') as file:
    vessels_data = json.load(file)

# Create a Folium map centered on a general global location
map_center = [20, 0]  # Latitude and Longitude for map center
m = folium.Map(location=map_center, zoom_start=2, tiles='CartoDB positron')

# Add CircleMarkers for each vessel
for vessel in vessels_data:
    latitude = float(vessel['LATITUDE'])
    longitude = float(vessel['LONGITUDE'])
    tooltip = f"Name: {vessel['NAME']}, MMSI: {vessel['MMSI']}, COG: {vessel['COG']}, SOG: {vessel['SOG']}"

    folium.CircleMarker(
        location=(latitude, longitude),
        radius=1,  # 1px size
        color='blue',
        fill=True,
        fill_color='blue',
        tooltip=tooltip
    ).add_to(m)

# Save the map to an HTML file
output_file_path = '/Users/jordantaylor/PycharmProjects/ais-data/ais_map.html'
m.save(output_file_path)

print(f"Map has been created and saved at {output_file_path}")
