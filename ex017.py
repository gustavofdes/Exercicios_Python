#Calcular o cateto oposto e o cateto adjacente usando modulos

from math import hypot

co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))

hip = hypot(co, ca)

print(f"O valor da hipotenusa desse triangulo sera: {hip:.2f}")
