dias = int(input("Quantos dias ficou com o carro? "))
km = float(input("Quantos km rodados? "))
pd = dias*60
pkm = km*0.15
valor = pd + pkm
print(f"O valor cobrado por dias sera R${pd:.2f}")
print(f"O valor cobrado por km rodados sera R${pkm:.2f}")
print("-"*20)
print(f"O valor total pelo aluguel do carro é de R${valor:.2f}")