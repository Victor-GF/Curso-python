print("-- Contador de Dólares --")

reais = float(input("Informe quantos reais você tem: "))
valorDoDolar = float(input("Informe o valor atual do dólar: "))

dolares = int(reais // valorDoDolar)

print("{} reais conseguem comprar {} dólares".format(reais, dolares))

