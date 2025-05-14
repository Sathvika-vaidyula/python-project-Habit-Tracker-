import requests
from datetime import datetime

# =============================
# Constants and Configuration
# =============================

# Pixela API endpoint for user creation
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

# Your unique token and username (keep your token private!)
TOKEN = 's3s3s3s3s3s3s3s3s3s3'
USERNAME = 'sathvika'
GRAPH_ID = 'graph1'  # ID to identify your graph

# Headers used for authentication in Pixela API
HEADERS = {
    'X-USER-TOKEN': TOKEN
}

# =============================
# 1. Create a Pixela User
# (Only run once when setting up)
# =============================

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',  # Must be 'yes'
    'notMinor': 'yes'              # Must be 'yes'
}

# Uncomment the following lines to create your user
# user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print("User creation response:", user_response.text)

# =============================
# 2. Create a Graph
# (Only run once to set up your graph)
# =============================

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',    # Graph name shown on website
    'unit': 'hours',           # Unit to track (e.g., hours of coding)
    'type': 'float',           # Data type: int or float
    'color': 'shibafu'         # Graph color (green)
}

# Uncomment the following lines to create your graph
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
# print("Graph creation response:", graph_response.text)

# =============================
# 3. Log Today’s Progress
# =============================

# Pixela expects date in YYYYMMDD format
today = datetime.now().strftime('%Y%m%d')

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# Ask the user how many hours they coded today
pixel_data = {
    'date': today,
    'quantity': input("How many hours did you code today?: ")
}

# Send the data to Pixela
pixel_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=HEADERS)
print("Pixel creation response:", pixel_response.text)

# =============================
# 4. Update a Pixel
# (Use this if you want to change the logged value)
# =============================

# Update today's entry to a new value if needed
update_data = {
    'quantity': '2.6'  # Example updated value
}

update_endpoint = f"{pixel_creation_endpoint}/{today}"
update_response = requests.put(url=update_endpoint, json=update_data, headers=HEADERS)
print("Pixel update response:", update_response.text)
