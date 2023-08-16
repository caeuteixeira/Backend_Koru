#Este script simula funcionalidades de banco de dados para o nosso projeto CRUD

#O dicionário é nosso repositorio principal
personagens = {
    1: {
    "nome": "Harry Potter",
    "raça": "Humano",
    "casa": "Grifinória",
    "altura": 1.80,
    "nascimento": "31/07/1980",
    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Harry_Potter.jpg/1024px-Harry_Potter.jpg"
    },
    2: {
    "nome": "Ron Weasley",
    "raça": "Humano",
    "casa": "Grifinória",
    "altura": 1.80,
    "nascimento": "01/03/1980",
    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Ron_Weasley.jpg/440px-Ron_Weasley.jpg"
    },
    3: {
    "nome": "Hermione Granger",
    "raça": "Humano",
    "casa": "Grifinória",
    "altura": 1.65,
    "nascimento": "19/09/1979",
    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Hermione_Granger.jpg/400px-Hermione_Granger.jpg"
    },
    4: {
    "nome": "Draco Malfoy",
    "raça": "Humano",
    "casa": "Sonserina",
    "altura": 1.80,
    "nascimento": "05/06/1980",
    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Drago_Malefoy.jpg/800px-Drago_Malefoy.jpg"
    }
}

#Esta função gera um novo id
def gerar_id():
    id = len(personagens) + 1
    return id

#Esta cria um novo personagem no dicionário
def criar_personagem(nome, raça, casa, altura, nascimento, imagem):
    personagens[gerar_id()] = {"nome":nome, "raça":raça, "casa": casa, "altura":altura, "nascimento": nascimento, "imagem":imagem}

#Esta retorna um dicionário para todos os persongens
def retornar_personagens():
    return personagens

#Esta retorna um único personagem
def retornar_personagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else:
        return {}

#Esta atualiza os dados de um único personagem
def atualizar_personagem(id:int, dados_personagem:dict):
    personagens[id] = dados_personagem

#Esta remove um personagem
def remover_personagem(id:int):
    del personagens[id]
