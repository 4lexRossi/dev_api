from flask import Flask, request
from flask_restful import Resource
import json

lista_habilidades = [
    {
    'id':'1', 'habilidade':'Python'
    },
    {
    'id':'2', 'habilidade':'Java'
    },
    {
    'id':'3', 'habilidade':'Flask'
    },
    {
    'id':'4', 'habilidade':'PHP'
    }
]
class Habilidade(Resource):
    def get(self):
        return lista_habilidades

class Habilidades(Resource):
    def post(self, id):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status':'sucesso', 'mensagem': 'Habilidade excluida'}