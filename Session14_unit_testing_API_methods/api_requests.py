import requests

response = requests.get('https://randomuser.me/api/')
print(response.status_code)
print(response.text)

response_json = response.json()
print(response_json['results'][0]['gender'])

first_result = response_json['results'][0]
print(first_result['name'], first_result['email'])