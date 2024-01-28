import requests
import json

url = service.scoring_uri
headers = {'Content-Type': 'application/json'}

with open('input_data.json', 'r') as file:
    data = json.load(file)

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print('Resultado da previsão:', result)
else:
    print('Falha na chamada do ponto de extremidade:', response.text)
