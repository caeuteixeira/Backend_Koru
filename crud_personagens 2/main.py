from flask import Flask, jsonify, request, redirect, url_for
import repositorio

app = Flask(__name__)

#ROTA PARA RETORNAR TODOS OS PERSONAGENS
@app.route("/personagens", methods=["GET"])
def get_personagens():
    lista_personagens = repositorio.retornar_personagens()
    return jsonify(lista_personagens)

#ROTA PARA RETORNAR UM ÚNICO PERSONAGEM
@app.route("/personagem/<int:id>", methods=["GET"])
def get_personagem(id):
    personagem: repositorio.retornar_personagem(id)

app.run(debug=True)