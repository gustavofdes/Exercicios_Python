vm = 80
v = int(input("Digite a velocidade de seu carro para saber se tomou multa ou não: "))
print(" "*20)

if v > vm:
    multa = v - vm
    print(f"Você passou o limite de velocidade de {vm}Km/h e recebeu uma multa")
    valor_multa = multa * 7
    print(f"Você recebeu uma multa de R${valor_multa} por passar {multa}Km/h do limite permitido")
else:
    print(f"Você estava dentro do limite de velocidade e não foi multado")
print("Obrigado por usar nosso PROGRAMA!")
