import requests

url = 'http://maryagiamah.pythonanywhere.com/api'

data = {'name': 'John Doe'}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
