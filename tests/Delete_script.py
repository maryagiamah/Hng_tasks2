import requests

person_id = 1  # Replace with an existing person ID

url = f'http://maryagiamah.pythonanywhere.com/api/{person_id}'

response = requests.delete(url)

print(response.status_code)
print(response.json())
