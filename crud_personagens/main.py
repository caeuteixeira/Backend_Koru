from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

#Verificar o que a nossa funcao retornar_personagens() devolve e se sao necessarias alteracoes
@app.route("/")
def home():
    lista_personagens = repositorio.retornar_personagens()
    return render_template("index.html", dados=lista_personagens)

#usar essa rota tanto para atualizar e excluir quanto para SALVAR um novo personagem
#verificar se nossas estruturas de dados precisam mudar!
@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editar_personagem(id):
    if request.method == 'POST':
        #quer dizer que o usuário está mandando dados
        if "excluir" in request.form:
            repositorio.remover_personagem(id)
            return redirect(url_for('home'))
        elif "salvar" in request.form:
            #personagem = {}
            #personagem['nome'] = request.form["nome"]
            #personagem['casa'] = request.form["casa"]
            #personagem['raca'] = request.form["raca"]
            #personagem['altura'] = request.form["altura"]
            #personagem['nascimento'] = request.form["nascimento"]
            #personagem['imagem'] = request.form["imagem"]

            id = request.form["nome"]
            nome = request.form["nome"]
            casa = request.form["casa"]
            raca = request.form["raca"]
            altura = request.form["altura"]
            nascimento = request.form["nascimento"]
            imagem = request.form["imagem"]

            dados_retornados = repositorio.retornar_personagem(id)
            if dados_retornados:
                repositorio.atualizar_personagem(id=id, nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)
            else:
                repositorio.criar_personagem(nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)

            #if id in repositorio.retornar_personagens().keys():
                #repositorio.atualizar_personagem(id, personagem)

            return redirect(url_for('home'))

    else:
        #retorna os dados de um personagem na página de cadastro
        id, nome, raca, casa, nascimento, altura, imagem = repositorio.retornar_personagem(id)
        #personagem['id'] = id
        #return render_template("cadastro.html", **personagem)
        return render_template("cadastro.html", id = id, nome = nome, raca = raca, casa = casa, nascimento = nascimento, altura = altura, imagem = imagem)
    
#@app.route("/personagem", methods=["GET", "POST"])
#def criar_personagem():
    #if request.method == "POST":
        #personagem = {}
        #personagem['nome'] = request.form["nome"]
        #personagem['casa'] = request.form["casa"]
        #personagem['raca'] = request.form["raca"]
        #personagem['altura'] = request.form["altura"]
        #personagem['nascimento'] = request.form["nascimento"]
        #personagem['imagem'] = request.form["imagem"]
        #repositorio.criar_personagem(**personagem)
        #return redirect(url_for('home'))


    #else:
        #return render_template('cadastro.html', id=repositorio)

app.run(debug=True)