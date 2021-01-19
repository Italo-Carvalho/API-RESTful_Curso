import requests

headers = {'Authorization': 'Token 8a6344e4b2b696f1189cae63d7b8c5fd812f96fa'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Curso editado com sucesso",
    "url": "http://www.sdasadasasd.com"
}

resultado = requests.put(url=f'{url_base_cursos}1/',
                         headers=headers,
                         data=curso_atualizado)

#testando codigo de status HTTP
assert resultado.status_code == 200

#Testando o Titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']
