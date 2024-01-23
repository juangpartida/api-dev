import requests
import json
from datetime import datetime, timedelta

# Calculate the current UTC timestamp
current_time = datetime.utcnow()

# Calculate the start time by subtracting 30 days from the current time
start_time = current_time - timedelta(days=30)

# Ensure that the difference between start and end is within 15 days
if (current_time - start_time).days > 15:
    start_time = current_time - timedelta(days=15)

# Convert both start and end times to Unix epoch timestamps
start_timestamp = int(start_time.timestamp())
end_timestamp = int(current_time.timestamp())

# Build the API URL with parameters
url = f'https://api.mindflash.com/api/v3/course/users?status=Completed&start={start_timestamp}&end={end_timestamp}'
api_key = 'place-api-key-here'  # Replace with your actual API key

headers = {
    'x-mindflash-apikey': api_key,  # Use the specific header expected by Mindflash
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))  # Pretty-print the JSON data
else:
    print(f'Failed to retrieve data: {response.status_code}')
    print(response.text)  # Print the error message from the server
