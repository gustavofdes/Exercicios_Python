#Pega um numero decimal e transforma o inteiro

import math
n = float(input("Digite um numero float para ver seu inteiro: "))
ni = math.trunc(n)
print(f"{ni} é o valor inteiro de {n}")
