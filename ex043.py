print("-="*20)
print("\033[36mMedidor de IMC\033[m")
print("-="*20)

peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura em cm: "))
alt = alt / 100
imc = peso / alt ** 2
print(f"Seu IMC (Indice de Massa Corporal) é de: {imc:.2f}")
if imc < 18.5:
    print("Você esta abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Você esta no peso ideal")
elif imc >= 25 and imc < 30:
    print("Você esta com sobrepeso")
elif imc >= 30 and imc < 40:
    print("Você esta com obesidade")
elif imc >= 40:
    print("Você esta com obesidade mórbida")