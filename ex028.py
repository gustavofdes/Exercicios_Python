import random
import time

print("-=-"*20)
print("Vou pensar em um numero de 0 a 5 e você tem que tentar acertar")
print("-=-"*20)
time.sleep(0.5)
print("Pensando...")
time.sleep(0.5)
numero = int(input("Qual numero você acha que eu pensei? "))

lista = [1, 2, 3, 4]
numero_sort = random.choice(lista)   #Também pode ser usado o .randint(que volta um numero aleatorio entre os numeros colocadors)

if numero == numero_sort:
    print(f"Parabéns! Eu pensei no numero {numero_sort} e você acertou")
else:
    print(f"Que pena! Eu pensei no numero {numero_sort} e você errou")
print("FIM!")