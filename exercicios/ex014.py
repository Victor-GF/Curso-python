from xml.dom.expatbuilder import FragmentBuilder


print("--    Conversor de Temperatura    --")

celsius  = float(input("Informe a temperatura em ºC: "))
fahrenheit = celsius * 9/5 + 32

print("{:.2f}ºC correspondem a {:.2f}F".format(celsius, fahrenheit))

