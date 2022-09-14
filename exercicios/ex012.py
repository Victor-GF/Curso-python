print("-- Aplicador de Desconto --")

preco = float(input("Digite o valor do preço do produto: R$"))
porcentagem = float(input("Digite a quantidade de desconto: %"))
desconto = (porcentagem / 100) * preco

print(
  "R${:.2f} terá R${:.2f} de desconto e seu valor final será R${:.2f}".format(
    preco, desconto, preco - desconto
  )
)
