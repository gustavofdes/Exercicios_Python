a = float(input(("Digite um numero: ")))
b = float(input(("Digite outro numero: ")))
c =  float(input(("Digite outro numero: ")))

#Descobrindo quem é o meno
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
print(f"O menor numero é: {menor:.0f}")

#Descobrindo quer é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f"O maior numero digitado foi: {maior:.0f}")