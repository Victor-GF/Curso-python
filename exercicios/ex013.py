print("-- Aplicador de Aumento --")

salario = float(input("Digite seu salário atual: R$"))
aumento = (15 / 100) * salario

print("A partir de agora o salário irá aumentar {:.2f}R$ e irá passar a ser {:.2f}R$".format(aumento, salario + aumento))

