casa = int(input("Qual o valor da casa? R$"))
salario = int(input("Qual o seu salario? R$"))
anos = int(input("Em quantos anos deseja pagar? "))

meses = anos * 12
prest = casa / meses
porcentagem = salario * (30/100)
print(porcentagem)
print(prest)

if prest >= porcentagem:
    print(f"Sua casa ficaria na prestação de R${prest:.2f} em {meses} meses")
    print(f"Seu pedido de emprestimo foi \033[31mNEGADO\033[m")
else:
    print(f"Sua casa ficaria na prestação de R${prest:.2f} em {meses} meses")
    print(f"Seu pedido de emprestimo foi \033[32mAPROVADO\033[m")
