import requests
import json

# Define the URL of your Flask API
api_url = 'http://52.90.1.136:5000/generate'

# Define the payload (data) to send with the POST request
payload = {
    'prompt': 'Write test function in python to test this link: http://www.hello.com. Add assertion for the response to be 200. Just write code with no explanation'
}

# Send the POST request
response = requests.post(api_url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse and print the JSON response
    response_data = response.json()
    print('Response from API:', response_data)
else:
    # Print the error if the request was not successful
    print(f'Error: {response.status_code} - {response.text}')
