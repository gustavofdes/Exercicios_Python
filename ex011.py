#Calcular a area de uma parede e quantidade necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input("Qual a largura da parede: "))
altura = float(input("Qual a altura da parede: "))

area = largura * altura
litros = area / 2

print(f"Para pintar {area}m² de parede, sera necessario usar {litros} litros de tinta.")
