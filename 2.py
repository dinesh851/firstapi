import requests

# Make a GET request to the API endpoint
response = requests.get('http://localhost:3000/hello')

# Print the response content as a string
print(response.text)
