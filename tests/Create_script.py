import requests

url = 'https://your-api-url.com/api'

data = {'name': 'John Doe'}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
