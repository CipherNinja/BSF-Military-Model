import folium

# Initialize the map centered on India
india_map = folium.Map(location=[22.3511, 78.6677], zoom_start=5)

# Categorized locations with different marker colors
resources = {
    "Airbases": {
        "color": "blue",
        "icon": "plane",
        "locations": [
            {"name": "Air Force Station Hindon", "coords": [28.6974, 77.4538]},
            {"name": "Air Force Station Jamnagar", "coords": [22.4707, 70.0577]},
        ]
    },
    "Dams": {
        "color": "green",
        "icon": "tint",
        "locations": [
            {"name": "Tehri Dam", "coords": [30.3900, 78.4800]},
            {"name": "Bhakra Dam", "coords": [31.4167, 76.4333]},
        ]
    },
    "Major Cities": {
        "color": "red",
        "icon": "info-sign",
        "locations": [
            {"name": "Delhi", "coords": [28.7041, 77.1025]},
            {"name": "Mumbai", "coords": [19.0760, 72.8777]},
        ]
    },
    "Power Stations": {
        "color": "orange",
        "icon": "flash",
        "locations": [
            {"name": "Kudankulam Nuclear Power Plant", "coords": [8.1634, 77.7284]},
            {"name": "Tarapur Atomic Power Station", "coords": [19.8638, 72.6523]},
        ]
    },
    "Military Outposts": {
        "color": "purple",
        "icon": "shield",
        "locations": [
            {"name": "Military Outpost Leh", "coords": [34.1526, 77.5771]},
            {"name": "Strategic Base Port Blair", "coords": [11.6234, 92.7265]},
        ]
    }
}

# Add markers for each resource type
for category, details in resources.items():
    for location in details["locations"]:
        folium.Marker(
            location=location["coords"],
            popup=f"<b>{category}:</b> {location['name']}",
            icon=folium.Icon(color=details["color"], icon=details["icon"]),
        ).add_to(india_map)

# Save the map as an HTML file
india_map.save("India_Resource_Map.html")

print("Map has been created! Open 'India_Resource_Map.html' to view.")
