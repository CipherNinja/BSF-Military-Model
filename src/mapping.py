import folium

# Initialize the map centered on India
india_map = folium.Map(location=[22.3511, 78.6677], zoom_start=5)

# Add markers for various locations (additional bases included)
locations = [
    {"name": "Airbase 1", "coords": [28.7041, 77.1025]},  # Delhi
    {"name": "Military Outpost 1", "coords": [26.9124, 75.7873]},  # Jaipur
    {"name": "Road Intersection", "coords": [19.0760, 72.8777]},  # Mumbai
    {"name": "Air Force Station Hindon", "coords": [28.6974, 77.4538]},  # Ghaziabad
    {"name": "Naval Base INS Kadamba", "coords": [14.8512, 74.1048]},  # Karwar
    {"name": "Air Force Station Jamnagar", "coords": [22.4707, 70.0577]},  # Jamnagar
    {"name": "Military Outpost Leh", "coords": [34.1526, 77.5771]},  # Leh
    {"name": "Strategic Base Port Blair", "coords": [11.6234, 92.7265]},  # Andaman and Nicobar Islands
]

# Add markers for each location
for location in locations:
    folium.Marker(
        location["coords"],
        popup=f"<b>{location['name']}</b>",
        icon=folium.Icon(color="blue", icon="info-sign"),  # Different color for variety
    ).add_to(india_map)

# Save the map as an HTML file
india_map.save("India_Map_With_Points_Extended.html")

print("Map has been created! Open 'India_Map_With_Points_Extended.html' to view.")
