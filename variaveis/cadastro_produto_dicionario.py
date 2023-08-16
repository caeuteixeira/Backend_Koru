def retornar_produto(produto):
    texto_saida = f"Nome: {produto['nome']}\nDescrição: {produto['descrição']}\nPeso: {produto['peso']}\nValor: {produto['valor']}\nLançamento: {produto['lançamento']}"
    return texto_saida

produto_principal = {}

#Iniciando a coleta de dados informados pelo usuário
produto_principal["nome"] = input("Por favor, infome o nome do produto: ")
produto_principal["descrição"] = input("Por favor, informe a descrição do produto: ")
produto_principal["lançamento"] = int(input("Por favor, informe o ano de laçamento do produto: "))
produto_principal["valor"] = float(input("Por favor, informe o valor do produto em reais: "))
produto_principal["peso"] = float(input("Por favor, infome o peso do produto em quilos: "))

print(retornar_produto(produto_principal))