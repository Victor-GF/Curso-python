print("-- Contador de Dólares --")

reais = float(input("Informe quantos reais você tem: R$"))
valorDoDolar = float(input("Informe o valor atual do dólar: U$"))

dolares = reais / valorDoDolar

print("R${:.2f} reais conseguem comprar U${:.2f} dólares".format(reais, dolares))

