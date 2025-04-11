import folium

# Initialize the map centered on India
india_map = folium.Map(location=[22.3511, 78.6677], zoom_start=5)

# Categorized locations (Defensive and Strategic)
locations = [
    # Airbases
    {"name": "Air Force Station Hindon", "coords": [28.6974, 77.4538], "type": "Airbase", "color": "blue"},
    {"name": "Air Force Station Jamnagar", "coords": [22.4707, 70.0577], "type": "Airbase", "color": "blue"},
    {"name": "Air Force Station Vishakhapatnam", "coords": [17.6868, 83.2185], "type": "Airbase", "color": "blue"},
    {"name": "Air Force Station Agra", "coords": [27.1767, 78.0081], "type": "Airbase", "color": "blue"},
    {"name": "Air Force Station Pathankot", "coords": [32.2649, 75.6499], "type": "Airbase", "color": "blue"},
    {"name": "Strategic Airbase Kolkata", "coords": [22.5726, 88.3639], "type": "Airbase", "color": "blue"},
    {"name": "Strategic Airbase Port Blair", "coords": [11.6234, 92.7265], "type": "Airbase", "color": "blue"},
    {"name": "Air Force Station Tezpur", "coords": [26.6228, 92.8000], "type": "Airbase", "color": "blue"},

    # Military Outposts
    {"name": "Military Outpost Leh", "coords": [34.1526, 77.5771], "type": "Military Outpost", "color": "purple"},
    {"name": "Military Outpost Srinagar", "coords": [34.0837, 74.7973], "type": "Military Outpost", "color": "purple"},
    {"name": "Troop Deployment Silchar", "coords": [24.8273, 92.7979], "type": "Troop Deployment", "color": "red"},
    {"name": "Troop Deployment Agartala", "coords": [23.8315, 91.2868], "type": "Troop Deployment", "color": "red"},
    {"name": "Military Base Shillong", "coords": [25.5788, 91.8933], "type": "Military Outpost", "color": "purple"},

    # Dams
    {"name": "Tehri Dam", "coords": [30.3900, 78.4800], "type": "Dam", "color": "green"},
    {"name": "Bhakra Dam", "coords": [31.4167, 76.4333], "type": "Dam", "color": "green"},
    {"name": "Nagarjuna Sagar Dam", "coords": [16.5746, 79.3186], "type": "Dam", "color": "green"},
    {"name": "Hirakud Dam", "coords": [21.5375, 83.8726], "type": "Dam", "color": "green"},

    # Energy Facilities
    {"name": "Kudankulam Nuclear Power Plant", "coords": [8.1634, 77.7284], "type": "Nuclear Plant", "color": "orange"},
    {"name": "Tarapur Atomic Power Station", "coords": [19.8638, 72.6523], "type": "Nuclear Plant", "color": "orange"},
    {"name": "Kalpakkam Nuclear Facility", "coords": [12.5115, 80.1937], "type": "Nuclear Plant", "color": "orange"},
    {"name": "Ramagundam Power Station", "coords": [18.7557, 79.4565], "type": "Thermal Power", "color": "orange"},

    # Radar Stations
    {"name": "Radar Station Chennai", "coords": [13.0827, 80.2707], "type": "Radar Station", "color": "darkblue"},
    {"name": "Radar Station Vishakhapatnam", "coords": [17.6868, 83.2185], "type": "Radar Station", "color": "darkblue"},
    {"name": "Radar Station Kolkata", "coords": [22.5726, 88.3639], "type": "Radar Station", "color": "darkblue"},
    
    # Strategic Locations
    {"name": "Strategic Base Guwahati", "coords": [26.1445, 91.7362], "type": "Strategic Location", "color": "black"},
    {"name": "Strategic Base Imphal", "coords": [24.8170, 93.9368], "type": "Strategic Location", "color": "black"},

    # Additional Troop Deployments
    {"name": "Troop Deployment Tura", "coords": [25.5147, 90.2037], "type": "Troop Deployment", "color": "red"},
    {"name": "Troop Deployment Dimapur", "coords": [25.8757, 93.7278], "type": "Troop Deployment", "color": "red"},
    {"name": "Troop Deployment Sikkim Border", "coords": [27.3389, 88.6065], "type": "Troop Deployment", "color": "red"},
]

# Add markers for each location
for loc in locations:
    folium.Marker(
        location=loc["coords"],
        popup=f"<b>{loc['name']}</b><br>Type: {loc['type']}",
        icon=folium.Icon(color=loc["color"], icon="info-sign"),
    ).add_to(india_map)

# Save the map to a file
india_map.save("Map_With_Strategic_Locations.html")

print("Map generated successfully! Open 'Map_With_Strategic_Locations.html' in your browser.")
