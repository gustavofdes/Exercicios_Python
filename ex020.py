#Sortear aa ordem dos alunos para apresentar o trabalho

from random import shuffle
a1 = str(input("Escreva o nome do primeiro aluno: "))
a2 = str(input("Escreva o nome do segundo aluno: "))
a3 = str(input("Escreva o nome do terceiro aluno: "))
a4 = str(input("Escreva o nome do quarto aluno: "))
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f"A ordem sorteada foi: \n {alunos}")
print(alunos)