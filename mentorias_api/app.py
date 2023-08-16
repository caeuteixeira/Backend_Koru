from flask import Flask, request, jsonify
from datetime import datetime
from mentor import Mentor
from mentorando import Mentorando
from mentoria import Mentoria
from db_connector import DBConnector

app = Flask(__name__)

db = DBConnector("mentorias.db")


#RETORNA TODOS OS MENTORES
@app.route("/mentores", methods=["GET"])
def get_mentores():
    mentores = Mentor.get_all(db.connect())
    return jsonify(mentores)

#RETORNA UM UNICO MENTOR PELO ID
@app.route("/mentores/<int:id_mentor>", methods=["GET"])
def get_mentor(id_mentor):
    mentor = Mentor.get_by_id(id_mentor, db.connect())
    if mentor:
        return jsonify(mentor.to_dict())
    else:
        return jsonify({"error": "Mentor não localizado"}), 404
    
#RETORNAR TODOS OS MENTORANDOS
@app.route("/mentorandos", methods=["GET"])
def get_mentorandos():
    mentorandos = Mentorando.get_all(db.connect())
    return jsonify(mentorandos)

#RETORNA UM ÚNICO MENTORANDO PELO ID
@app.route("/mentorandos/<int:id_mentorando>", methods=["GET"])
def get_mentorando(id_mentorando):
    mentorando = Mentorando.get_by_id(id_mentorando, db.connect())
    if mentorando:
        return jsonify(mentorando.to_dict())
    else:
        return jsonify({"error": "Mentorando não localizado"}), 404
    
#RETORNAR TODAS AS MENTORIAS
@app.route("/mentorias", methods=["GET"])
def get_mentorias():
    mentorias = Mentoria.get_all(db.connect())
    return jsonify(mentorias)

#RETORNAR UM UNICA MENTORIA PELO ID
@app.route("/mentorias/<int:id_mentoria>", methods=["GET"])
def get_mentoria(id_mentoria):
    mentoria = Mentoria.get_by_id(id_mentoria, db.connect())
    if mentoria:
        return jsonify(mentoria.to_dict())
    else:
        return jsonify({"error": "Mentoria não localizada"}), 404
    

#CRIAR UM UNICO MENTOR
@app.route("/mentores", methods=["POST"])
def create_mentor():
    data = request.get_json()
    mentor = Mentor(nome=data["nome"], linkedin=data["linkedin"])
    mentor.save(db.connect())
    return jsonify(mentor.to_dict())

#CRIAR UM ÚNICO MENTORANDO
@app.route("/mentorando", methods=["POST"])
def create_mentorando():
    data = request.get_json()
    mentorando = Mentorando(nome=data["nome"], linkedin=data["linkedin"])
    mentorando.save(db.connect())
    return jsonify(mentorando.to_dict())

#CRIAR UMA UNICA MENTORIA
@app.route("/mentorias", methods=["POST"])
def create_mentoria():
    data = request.get_json()
    mentor = Mentor.get_by_id(data['id_mentor'], db.connect())
    mentorando = Mentorando.get_by_id(data['id_mentorando'], db.connect())
    data_mentoria = datetime.fromisoformat(data['data_mentoria'])
    mentoria = Mentoria(mentor=mentor, mentorando=mentorando, data=data_mentoria)
    mentoria.save(db.connect())
    return jsonify(mentoria.to_dict())

#ATUALIZAR UM ÚNICO MENTOR
@app.route("/mentores/<int:id_mentor>", methods=["PUT"])
def update_mentor(id_mentor):
    data = request.get_json()
    mentor = Mentor.get_by_id(id_mentor, db.connect())
    if mentor:
        mentor.nome = data ['nome']
        mentor.linkedin = data['linkedin']
        mentor.save(db.connect())
        return jsonify(mentor.to_dict())
    else:
        return jsonify({'error' : "Mentor não encontrado"}), 404

#ATUALIZAR UM ÚNICO MENTORANDO
@app.route("/mentorandos/<int:id_mentorando>", methods=["PUT"])
def update_mentorando(id_mentorando):
    data = request.get_json()
    mentorando = Mentorando.get_by_id(id_mentorando, db.connect())
    if mentorando:
        mentorando.nome = data ['nome']
        mentorando.linkedin = data['linkedin']
        mentorando.save(db.connect())
        return jsonify(mentorando.to_dict())
    else:
        return jsonify({'error' : 'Mentorando não encontrado'}), 404

#ATUALIZAR UMA UNICA MENTORIA
@app.route("/mentorias/<int:id_mentoria>", methods=["PUT"])
def update_mentoria(id_mentoria):
    data = request.get_json()
    mentoria = Mentoria.get_by_id(id_mentoria, db.connect())
    if mentoria:
        mentor = Mentor.get_by_id(data['id_mentor'], db.connect())
        mentorando = Mentorando.get_by_id(data['id_mentorando'], db.connect())
        data_mentoria = datetime.fromisoformat(data['data'])
        mentoria.mentor = mentor
        mentoria.mentorando = mentorando
        mentoria.data = data_mentoria
        mentoria.save(db.connect())
        return jsonify(mentoria.to_dict())
    else:
        return jsonify({'error' : 'Mentoria não encontrada'}), 404

#REMOVER UM ÚNICO MENTOR
@app.route("/mentores/<int:id_mentor>", methods=["DELETE"])
def delete_mentor(id_mentor):
    mentor = Mentor.get_by_id(id_mentor, db.connect())
    if mentor:
        mentor.delete(db.connect())
        return '', 204
    else:
        return jsonify({'error': 'Mentor não localizado'}), 404

#REMOVER UM ÚNICO MENTORANDO
@app.route("/mentorandos/<int:id_mentorando>", methods=["DELETE"])
def delete_mentorando(id_mentorando):
    mentorando = Mentorando.get_by_id(id_mentorando, db.connect())
    if mentorando:
        mentorando.delete(db.connect())
        return '', 204
    else:
        return jsonify({'error': 'Mentorando não localizado'}), 404

#REMOVER UMA ÚNICA MENTORIA
@app.route("/mentorias/<int:id_mentoria>", methods=["DELETE"])
def delete_mentoria(id_mentoria):
    mentoria = Mentoria.get_by_id(id_mentoria, db.connect())
    if mentoria:
        mentoria.delete(db.connect())
        return '', 204
    else:
        return jsonify({'error': 'Mentoria não localizado'}), 404
    

app.run(debug=True)