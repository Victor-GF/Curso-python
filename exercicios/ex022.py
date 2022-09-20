nome = input("Insira seu nome completo: ")

print(nome.upper())
print(nome.lower())
print("O nome possui {} letras".format(len(nome) - nome.count(" ")))
print("A primeira palavra possui {} letras".format(len(nome.split()[0])))

