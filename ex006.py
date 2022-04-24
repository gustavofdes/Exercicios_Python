#Criar algoritimo que mostre o triplo, o dobro e a raiz quadrada do numero digitado
n = int(input("Digite um numero: "))

d = n * 2
t = n * 3
rq = n ** (1/2)

print(f"o dobro desse numero é {d}")
print(f"O triplo desse numero é {t}")
print("A raiz quadrada desse numero é {:.3f}".format(rq)) #esse {:.3f} é para colocar um limite no float
