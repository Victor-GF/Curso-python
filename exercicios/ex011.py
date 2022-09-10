print("-- Rendimento de Tinta --")

largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))
area = largura * altura

litrosDeTinta = area / 2
print("Para uma área de {} metros² serão necessários {} litros de tinta".format(area, litrosDeTinta))

