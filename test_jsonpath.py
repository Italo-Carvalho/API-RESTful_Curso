import requests
import jsonpath

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

#resutaldos = jsonpath.jsonpath(avaliacoes.json(), 'results')
#primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
#nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].name')[0]

#Todos os nomes das pessoas que avaliaram o curso

names = jsonpath.jsonpath(avaliacoes.json(), 'results[*].name')
print(names)
