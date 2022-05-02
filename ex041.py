from datetime import date
ano = date.today().year
nasc = int(print("Ano de nascimento do atleta: "))
idade = ano - nasc

if idade < 9:
    print("Categoria: Mirim")
elif idade >= 9 and idade < 14:
    print("Categoria: Infantil")
