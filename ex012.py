#Algorito que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input("Preço do produto: R$"))
d = int(input("Valor da % descontada: "))

vf = p - (d/100) * p

print(f"Esse produto de R${p} com um desconto de {d}%, ficara por R${vf:.2f}.")

#Eu fiz o valor do desconto tbm ser digitado