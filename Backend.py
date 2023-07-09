import requests

# GraphQL query as a string
query = """
{
  user(id: 1) {
    name
    email
  }
}
"""
url, headers = 'https://api.example.com/graphql', {'Content-Type': 'application/json'}

# JSON payload
payload = {'query': query}

# GET request
response, json_response = requests.get(url, headers=headers, params=payload), response.json()
print(json_response['data'])
