nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("\033[31mREPROVADO\033[m")
    print(f"O aluno tirou {media:.1f} de média.")
  
elif media >= 5 and media < 6.9:
    print("\033[33mRECUPERAÇÃO\033[m")
    print(f"O aluno tirou {media:.1f} de média.")

elif media > 7:
    print("\033[32mAPROVADO\033[m")
    print(f"O aluno tirou {media:.1f} de média.")