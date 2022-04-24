salario = float(input("Digite seu salario para contabilizar seu aumento: R$"))

if salario > 1250.00:
    ns = salario + (10/100) * salario
else:
    ns = salario + (15/100) * salario
print(f"O seu salario tera um aumento e agora sera: \033[32mR${ns:.2f}")
