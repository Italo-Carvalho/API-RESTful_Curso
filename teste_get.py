import requests

headers = {'Authorization': 'Token 07ccaf37157a708e9f0140a5d5a9fd4aa3cf91ac'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

#print(resultado.json())

#Testando se o endpoint está correto
assert resultado.status_code == 200

#Testando a quantidade de registros
assert resultado.json()['count'] == 7

#Tesntato se o titulo do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Como bater carteira'
