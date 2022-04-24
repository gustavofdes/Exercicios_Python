#Algoritmo que leia o salario de um funcionario com o aumento de 15%

salario = float(input("Valor do salario atual: R$"))

ns = salario + (15/100) * salario

print(f"O seu novo salario com o aumento de 15% sera de R${ns:.2f}")
