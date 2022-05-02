import datetime
from time import sleep
nasc = int(input("Digite a data de nascimento: "))
ano = datetime.date.today().year 
idade = ano - nasc
sleep(0.4)
if idade > 18:
    print("\033[31mVocê ja passou da hora de se alistar!\033[m")
    al = nasc + 18
    print(f"Você ja passou \033[31m{ano - al} \033[manos de se alistar")
elif idade < 18:
    print("\033[32mAinda não é sua hora de se alistar!\033[m")
    al = nasc + 18
    print(f"Ainda faltam \033[32m{al - ano} \033[mano(s) para se alistar")
elif idade == 18:
    print("\033[33mVocê esta na hora de se alistar! \033[m")