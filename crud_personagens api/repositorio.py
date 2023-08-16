from datetime import datetime
import sqlite3
#Este script simula funcionalidades de banco de dados para o nosso projeto CRUD

#O dicionário é nosso repositorio principal
personagens = {
    1: {
    "nome": "Harry Potter",
    "raca": "Humano",
    "casa": "Grifinória",
    "altura": 1.80,
    "nascimento": "31/07/1980",
    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Harry_Potter.jpg/1024px-Harry_Potter.jpg"
    },
    2: {
    "nome": "Ron Weasley",
    "raca": "Humano",
    "casa": "Grifinória",
    "altura": 1.80,
    "nascimento": "01/03/1980",
    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Ron_Weasley.jpg/440px-Ron_Weasley.jpg"
    },
    3: {
    "nome": "Hermione Granger",
    "raca": "Humano",
    "casa": "Grifinória",
    "altura": 1.65,
    "nascimento": "19/09/1979",
    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Hermione_Granger.jpg/400px-Hermione_Granger.jpg"
    },
    4: {
    "nome": "Draco Malfoy",
    "raca": "Humano",
    "casa": "Sonserina",
    "altura": 1.80,
    "nascimento": "05/06/1980",
    "imagem": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Drago_Malefoy.jpg/800px-Drago_Malefoy.jpg"
    }
}

#tratamento de datas
def tratar_iso_para_dmy(data:str):
    if "-" in data:
        data = datetime.strptime(data, '%Y-%m-%d')
        return data.strftime('%d/%m/%Y')
    else:
        return data

def tratar_dmy_para_iso(data:str):
    if "/" in data:
        data = datetime.strptime(data, '%d/%m/%Y')
        return data.strftime('%Y-%m-%d')
    else:
        return data

#Esta função gera um novo id
def gerar_id():
    conn = sqlite3.connect("harry_potter.db")
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='personagens'")
    next_id = cursor.fetchone()[0]
    return next_id +1

#Esta cria um novo personagem no dicionário
def criar_personagem(nome, raca, casa, altura, nascimento, imagem):
    try:
        conn = sqlite3.connect("harry_potter.db")
        cursor = conn.cursor()
        sql_insert = "INSERT INTO personagens (nome_personagem, raca_personagem, casa_personagem, altura_personagem, nascimento_personagem, imagem_personagem) values (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (nome, raca, casa, altura, nascimento, imagem))
        personagem_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return personagem_id
    except Exception as ex:
        print(ex)
        return 0

#Esta retorna um dicionário para todos os persongens
def retornar_personagens():

    try:
        resultado = []
        conn = sqlite3.connect("harry_potter.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM personagens"
        cursor.execute(sql_select)
        personagens = cursor.fetchall()
        conn.close()
        for item in personagens:
            personagem = {
                'id': item[0],
                'nome': item[1],
                'raca': item[2],
                'casa': item[3],
                'nascimento': item[4],
                'altura': item[5],
                'imagem': item[6]
            }
            resultado.append(personagem)

        return resultado
    
    except:
        return False

#Esta retorna um único personagem
def retornar_personagem(id:int):
    try:
        if id == 0:
            return gerar_id(), "", "", "", "", "", ""
        conn = sqlite3.connect("harry.potter.db")
        cursor = conn.cursor()

        sql_select = "SELECT * FROM personagens WHERE id_personagem = ?"
        cursor.execute (sql_select, (id, ))
        id, nome, raca, casa, nascimento, altura, imagem = cursor.fetchone()
        conn.close()
        return {"id": id,
                "nome": nome, 
                "raca": raca,
                "casa": casa,
                "nascimento": nascimento, 
                "altura": altura,
                "imagem": imagem
                }
    
    except:
        return False

#Esta atualiza os dados de um único personagem
def atualizar_personagem(id:int, nome, raca, casa, altura, nascimento, imagem):
    try:
        conn = sqlite3.connect("harry_potter.db")
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET nome_personagem = ?, raca_personagem = ?, casa_personagem = ?, altura_personagem = ?, nascimento_personagem = ?, imagem_personagem = ? WHERE id_personagem = ?"
        cursor.execute(sql_update, (nome, raca, casa, altura, nascimento, imagem, id))
        conn.commit()
        conn.close()
        return True
    
    except Exception as ex:
        print(ex)
        return False

#Esta remove um personagem
def remover_personagem(id:int):
    try:
        conn = sqlite3.connect("harry_potter.db")
        cursor = conn.cursor()
        sql_delete = "DELETE FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    
    except Exception as ex:
        print(ex)
        return False

