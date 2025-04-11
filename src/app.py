from flask import Flask, request, jsonify, send_file
import heapq
from geopy.distance import geodesic

app = Flask(__name__)

# Strategic resources for a war scenario
resources = [
    # Airbases
    {"name": "Air Force Station Hindon", "coords": [28.6974, 77.4538], "type": "Airbase"},
    {"name": "Air Force Station Jamnagar", "coords": [22.4707, 70.0577], "type": "Airbase"},
    {"name": "Air Force Station Vishakhapatnam", "coords": [17.6868, 83.2185], "type": "Airbase"},
    {"name": "Air Force Station Agra", "coords": [27.1767, 78.0081], "type": "Airbase"},
    {"name": "AWACS Base Chennai", "coords": [13.0827, 80.2707], "type": "AWACS Base"},

    # Military Outposts
    {"name": "Military Outpost Leh", "coords": [34.1526, 77.5771], "type": "Military Outpost"},
    {"name": "Military Outpost Srinagar", "coords": [34.0837, 74.7973], "type": "Military Outpost"},
    {"name": "Ground Troop Deployment Siliguri", "coords": [26.7271, 88.3953], "type": "Ground Troop Deployment"},
    {"name": "Submarine Base Visakhapatnam", "coords": [17.6868, 83.2185], "type": "Submarine Base"},

    # Naval Bases and Aircraft Carriers
    {"name": "Naval Base INS Kadamba", "coords": [14.8512, 74.1048], "type": "Naval Base"},
    {"name": "Aircraft Carrier INS Vikrant", "coords": [15.2993, 74.1240], "type": "Aircraft Carrier"},
    {"name": "Naval Base Port Blair", "coords": [11.6234, 92.7265], "type": "Naval Base"},

    # Energy Facilities
    {"name": "Kudankulam Nuclear Power Plant", "coords": [8.1634, 77.7284], "type": "Nuclear Plant"},
    {"name": "Ramagundam Power Station", "coords": [18.7557, 79.4565], "type": "Thermal Power Plant"},

    # Radar Stations
    {"name": "Radar Station Kolkata", "coords": [22.5726, 88.3639], "type": "Radar Station"},
    {"name": "Radar Station Chandigarh", "coords": [30.7333, 76.7794], "type": "Radar Station"},

    # Dams
    {"name": "Tehri Dam", "coords": [30.3900, 78.4800], "type": "Dam"},
    {"name": "Bhakra Dam", "coords": [31.4167, 76.4333], "type": "Dam"},

    # Dummy Deployments
    {"name": "Missile Defense Installation Delhi", "coords": [28.7041, 77.1025], "type": "Missile Defense"},
    {"name": "Submarine INS Arihant Deployment", "coords": [11.6234, 92.7265], "type": "Submarine Deployment"},
]

# Helper function to calculate nearest locations
def find_nearest_locations(pinned_coords):
    distances = []
    for resource in resources:
        distance = geodesic(pinned_coords, resource["coords"]).km
        distances.append((distance, resource))
    return heapq.nsmallest(3, distances, key=lambda x: x[0])

@app.route('/')
def serve_map():
    # Serve the enhanced Leaflet-based map
    return send_file(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\BSF-Military-Model\src\templates\Leaflet_Map.html")

@app.route('/process-location', methods=['POST'])
def process_location():
    data = request.json  # Receive the pinned coordinates from the frontend
    pinned_coords = data.get("coords")

    # Debugging: Print the pinned location
    print(f"User pinned location: {pinned_coords}")

    # Find nearest strategic locations
    nearest = find_nearest_locations(pinned_coords)

    # Return the nearest locations
    response = {
        "message": "Nearest locations calculated successfully!",
        "nearest": [
            {"name": loc[1]["name"], "type": loc[1]["type"], "distance": f"{loc[0]:.2f} km"}
            for loc in nearest
        ],
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
