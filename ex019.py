#Sortear um nome de aluno aleatorio para apagar o quadro

from random import choice
a1 = str(input("Escreva o nome do primeiro aluno: "))
a2 = str(input("Escreva o nome do segundo aluno: "))
a3 = str(input("Escreva o nome do terceiro aluno: "))
a4 = str(input("Escreva o nome do quarto aluno: "))

alunos = [a1, a2, a3, a4]
sorteado = choice(alunos)
print(f"O aluno sorteado para apagar o quadro foi: {sorteado}")