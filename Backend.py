from re import search

import requests


def hackerrankInString(s):
    target_match = r'h\w*a\w*c\w*k\w*e\w*r\w*r\w*a\w*n\w*k'
    match = search(target_match, s)
    result = 'YES' if match else 'NO'
    return result


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
