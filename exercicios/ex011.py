print("-- Rendimento de Tinta --")

largura = float(input("Informe a largura da parede em metros: "))
altura = float(input("Informe a altura da parede em metros: "))
area = largura * altura

litrosDeTinta = area / 2
print("Para uma área de {}m² serão necessários {:.1f} litros de tinta".format(area, litrosDeTinta))

