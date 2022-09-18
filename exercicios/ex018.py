from math import tan, sin, cos, radians

angulo = radians(float(input("-> Informe o valor do ângulo em graus: ")))

print(
  """>> O SENO é: {:.2f}
>> O COSSENO é: {:.2f}
>> A TANGENTE é: {:.2f}""".format(sin(angulo), cos(angulo), tan(angulo))
)

