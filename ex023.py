#numero = str((input("Digite um numero de 0 a 9999: "))).strip()
#numero = "000" + numero
#print(f"Unidade: {numero[-1]}") #Quando utilizado o -1 ele faz a contagem da direita para a esquerda
#print(f"Dezena: {numero[-2]}")
#print(f"Centena: {numero[-3]}")
#print(f"Milhar: {numero[-4]}")
#print("-"*25)


#Forma do video:
num = float(input("Digite um numero de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Unidade {u:.0f}")
print(f"Dezena: {d:.0f}")
print(f"Centena: {c:.0f}")
print(f"Milhar: {m:.0f}")
