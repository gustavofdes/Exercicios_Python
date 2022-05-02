n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    print(f"O numero \033[32m{n1:.1f}\033[m é maior que o numero \033[32m{n2:.1f}\033[m")

elif n2 > n1:
    print(f"O numero \033[32m{n2:.1f}\033[m é maior que o numero \033[32m{n1:.1f}\033[m")

elif n1 == n2:
    print(f"Não existe numero maior, o numero \033[32m{n1:.1f}\033[m e \033[32m{n2:.1f}\033[m sao iguais")
