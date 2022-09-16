print("--   Aluguel de veículos   --")

km = float(input("Quantos Km rodados: "))
dias = int(input("Quantos dias de aluguel: "))

preco = 60 * dias + 0.15 * km

print("O valor a ser pago do aluguel é de {:.2f}R$".format(preco))

