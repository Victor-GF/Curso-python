print("-- Aplicador de Desconto --")

preco = float(input("Digite o valor do preço do produto: "))
desconto = (5 / 100) * preco

print("O valor {} terá {} reais de desconto e seu valor final será {}".format(preco, desconto, preco - desconto))

