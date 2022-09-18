from emoji import emojize
from math import sqrt

print(emojize("--  Calculadora de Hipotenusa :cat_face:  --"))

catOposto = float(input("Informe o valor do cateto oposto: "))
catAdjacente = float(input("Informe o valor do cateto adjacente: "))
hipotenusa = sqrt(catOposto ** 2 + catAdjacente ** 2)

print("O valor da Hipotenusa é: {:.2f}".format(hipotenusa))

