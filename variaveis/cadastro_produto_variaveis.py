def exibir_produto():
    print(f"Nome: {nome_produto}")
    print(f"Descrição: {descricao_produto}")
    print(f"Peso: {peso_produto}")
    print(f"Valor: {valor_produto}")
    print(f"Lançamento: {ano_lancamento_produto}")

def retornar_produto():
    texto_saida = f"Nome: {nome_produto}\nDescrição: {descricao_produto}\nPeso: {peso_produto}\nValor: {valor_produto}\nLançamento: {ano_lancamento_produto}"
    return texto_saida

print("cadastro de produtos")

#Iniciando a coleta de dados informados pelo usuário
nome_produto = input("Por favor, infome o nome do produto: ")
descricao_produto = input("Por favor, informe a descrição do produto: ")
ano_lancamento_produto = int(input("Por favor, informe o ano de laçamento do produto: "))
valor_produto = float(input("Por favor, informe o valor do produto em reais: "))
peso_produto = float(input("Por favor, infome o peso do produto em quilos: "))

print(retornar_produto())