distancia = float(input("Qual foi a distâcia de sua viagem? "))

if distancia >= 200:
    valor = distancia * 0.45
    print(f"O valor a ser pago pela viagem é de R${valor:.2f}")
else:
    valor = distancia * 0.50
    print(f"O valor a ser pago pela viagem é de R${valor:.2f}")