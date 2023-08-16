import sqlite3

#Conectar com o banco de dados
conexao = sqlite3.connect('harry_potter.db')

#Criando os dados que vou manipular no banco
nome = "Ron Weasley"
raca = "Humano"
casa = "Grifinória"
altura = 1.80
nascimento = "01/03/1980"
imagem = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Ron_Weasley.jpg/440px-Ron_Weasley.jpg"

cursor = conexao.cursor()
sql_delete = "DELETE from personagens WHERE id_personagem = ?"
cursor.execute(sql_delete, (1, ))

sql_select_unico = "SELECT * FROM personagens WHERE id_personagem = ?"
cursor.execute(sql_select_unico, (1, ))
print(cursor.fetchone())