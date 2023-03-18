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
url = 'https://api.example.com/graphql'

headers = {'Content-Type': 'application/json'}

# JSON payload
payload = {'query': query}

# GET request with the query payload and headers
response = requests.get(url, headers=headers, params=payload)

json_response = response.json()

print(json_response['data'])
