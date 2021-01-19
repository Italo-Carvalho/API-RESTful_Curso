import requests

headers = {'Authorization': 'Token 07ccaf37157a708e9f0140a5d5a9fd4aa3cf91ac'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Curso de kaquitupiju",
    "url": "http://www.geektop.com"
}

resultado = requests.post(url=url_base_cursos,
                          headers=headers,
                          data=novo_curso)

#Testando o codigo de status HTTP 201

assert resultado.status_code == 201

#Testando se o titulo do curso retornado e o mesmo informado

assert resultado.json()['titulo'] == novo_curso['titulo']
