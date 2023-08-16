import sqlite3

produtos = {
    1: {
        "nome": "Iphone 14 PRO",
        "peso": "172g",
        "preco": 7800.00,
        "descricao": "Iphone 14, modelo PRO MAX, na cor vermelha",
        "fornecedor": "Apple"
    },
    2: {
        "nome": "Samsung Galaxy S21",
        "peso": "200g",
        "preco": 5500.00,
        "descricao": "Samsung Galaxy S21, modelo com 5G, na cor preta",
        "fornecedor": "Samsung"
    },
    3: {
        "nome": "MacBook Pro",
        "peso": "1.62kg",
        "preco": 15999.00,
        "descricao": "MacBook Pro 16 polegadas, processador M1 Max, na cor prata",
        "fornecedor": "Apple"
    },
    4: {
        "nome": "Sony PlayStation 5",
        "peso": "4.5kg",
        "preco": 4499.00,
        "descricao": "Console Sony PlayStation 5, com controle DualSense, na cor branca",
        "Fornecedor": "Sony"
    },
    5: {
        "nome": "Amazon Echo Dot",
        "peso": "300g",
        "preco": 349.00,
        "descricao": "Caixa de som inteligente Amazon Echo Dot, com assistente virtual Alexa, na cor azul",
        "fornecedor": "Amazon"
    },
    6: {
        "nome": "Nvidia GeForce RTX 3080",
        "peso": "1.5kg",
        "preco": 7299.00,
        "descricao": "Placa de vídeo Nvidia GeForce RTX 3080, 10GB GDDR6X, na cor preta",
        "fornecedor": "Nvidia"
    }
}

#id generator
def gerar_id():
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='produtos'")
    id = cursor.fetchone()[0]
    conn.close()
    return id + 1

#create
def criar_produto(nome:str, peso:str, preco:float, descricao:str, fornecedor:str):
    try:
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_insert = "INSERT INTO produtos (nome_produto, peso_produto, preco_produto, descricao_produto, fornecedor_produto) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (nome, peso, preco, descricao, fornecedor))
        id = cursor.lastrowid
        conn.commit()
        conn.close()
        return id
    except Exception as ex:
        print(ex)
        return 0

#update
def atualizar_produto(id:int, nome:str, peso:str, preco:float, descricao:str, fornecedor:str):
    try:
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_update = "UPDATE produtos SET nome_produto = ?, peso_produto = ?, preco_produto = ?, descricao_produto = ?, fornecedor_produto = ? WHERE id_produto = ?"
        cursor.execute(sql_update, (nome, peso, preco, descricao, fornecedor, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
    
#delete
def remover_produto(id:int):
    try:
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_delete = "DELETE FROM produtos WHERE id_produto = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

#read
def retornar_produto(id:int) -> tuple: 
    try:
        if id == 0:
            return gerar_id(), "", "", "", "", ""
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM produtos WHERE id_produto = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, peso, preco, descricao, fornecedor = cursor.fetchone()
        
        conn.close()
        return {'id':id,'nome':nome, 'peso': peso, 'preco': preco, 'descicao': descricao,'fornecedor': fornecedor}
    except Exception as ex:
        print(ex)
        return False

def retornar_produtos() -> dict:
    try:
       
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM produtos"
        cursor.execute(sql_select)
        dados = cursor.fetchall() #Aqui colocamos na variável DADOS uma lista de tuplas retornada pelo banco de dados        
        conn.close()
        produtos = [] #Criamos uma lista vazia, para que depois nossa função possa retorná-la

        for item in dados: #Para cada TUPLA contida na lista retornado do banco, vamos criar um dicionário e alimenta lo com os dados do produto
            produto = {}
            produto['id'] = item [0]
            produto['nome'] = item [1]
            produto['peso'] = item [2]
            produto['preco'] = item [3]
            produto['descricao'] = item [4]
            produto['fornecedor'] = item [5]
            produtos.append(produto) #Ao final de cada volta do loop, vamos colocar dicionário do produto que acabou de ser preenchido dentro da lista que foi criada

        return produtos
    except Exception as ex:
        print(ex)
        return False