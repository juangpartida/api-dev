import requests
import json

url = 'https://api.mindflash.com/api/v3/user'
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
