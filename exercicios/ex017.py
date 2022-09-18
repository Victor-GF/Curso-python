from emoji import emojize
from math import hypot

print(emojize("--  Calculadora de Hipotenusa :cat_face:  --"))

catOposto = float(input("-> Informe o valor do cateto oposto: "))
catAdjacente = float(input("-> Informe o valor do cateto adjacente: "))
hipotenusa = hypot(catOposto, catAdjacente)

print(">> O valor da Hipotenusa é: {:.2f}".format(hipotenusa))

