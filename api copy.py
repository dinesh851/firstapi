import requests
import json

# Make a GET request to the API endpoint
response = requests.get('http://localhost:3000/hello')

# Print the response content as a string
print(response.text)

# Define the base URL for our API
base_url = 'http://localhost:3000'

# Define some sample data to use in our requests
user_data = {'name': 'John', 'email': 'john@example.com'}

# Make a PUT request to update a user record
user_id = 123
put_url = f'{base_url}/users/{user_id}'
response = requests.put(put_url, json=user_data)
if response.status_code == 200:
    print(response.text)
else:
    print(f'Error updating user record: {response.status_code}')

# Make a POST request to create a new user record
post_url = f'{base_url}/users'
response = requests.post(post_url, json=user_data)
if response.status_code == 200:
    print(response.text)
else:
    print(f'Error creating user record: {response.status_code}')