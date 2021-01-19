import requests

#GET Avaliações

#avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')
#print(avaliacoes.status_code)
#print(avaliacoes.json())
#print(avaliacoes.json()['count'])
#print(avaliacoes.json()['results'])
#print(avaliacoes.json()['results'][1]['name'])

#GET Cursos

headers = {'Authorization': 'Token 07ccaf37157a708e9f0140a5d5a9fd4aa3cf91ac'}
cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/',
                      headers=headers)
print(cursos.status_code)