import requests

# Define the GraphQL query as a string
query = """
{
  user(id: 1) {
    name
    email
  }
}
"""

# Define the GraphQL endpoint URL
url = 'https://api.example.com/graphql'

# Define the request headers
headers = {'Content-Type': 'application/json'}

# Define the request payload as a JSON object
payload = {'query': query}

# Send the GET request with the query payload and headers
response = requests.get(url, headers=headers, params=payload)

# Extract the JSON response from the request
json_response = response.json()

# Print the response data
print(json_response['data'])
