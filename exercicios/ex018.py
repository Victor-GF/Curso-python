from math import tan, sin, cos, radians

angulo = radians(float(input("Informe o valor do ângulo em graus: ")))

print(
  """  O seno é: {:.2f}
  O cosseno é: {:.2f}
  A tangente é: {:.2f}""".format(sin(angulo), cos(angulo), tan(angulo))
)

