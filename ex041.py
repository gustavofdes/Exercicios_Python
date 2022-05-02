from datetime import date
ano = date.today().year
nasc = int(input("Ano de nascimento do atleta: "))
idade = ano - nasc
print(idade)
if idade < 9:
    print("Categoria: Mirim")

elif idade >= 9 and idade < 14:
    print("Categoria: Infantil")

elif idade >= 14 and idade < 19:
    print("Categoria: Junior")

elif idade >= 19 and idade < 20:
    print("Categoria: Senior")
    
elif idade >= 20:
    print("Categoria: Master")
