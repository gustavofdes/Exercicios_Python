
import random
import time

print("\033[34m-="*38)
print("Ola! Seja bem-vindo ao nosso programa! Escolha a opção que deseja usar: ")
print("-=" * 38 + "\033[m")
time.sleep(0.5)

print("\033[30mJogo de advinhação --> \033[32m1\033[m")
print("\033[30mTabuada --> \033[32m2\033[m")
print("\033[30mVerificador de multa --> \033[32m3\033[m")

opcao = int(input("\033[34mEscolha com a opção desejada: "))
print("\033[31mAGUARDE...\033[m")
time.sleep(1)

if opcao == 1:
    print("")
    print("A opção selecionada foi \033[4:36mJogo de Adivinhação\033[m !")
    print("Vou pensar em um numero de 0 a 5 e você tem que acertar qual eu pensei...")
    time.sleep(0.5)
    sorteado = random.randint(1, 5)
    print("Pensando...")
    time.sleep(2.5)
    number = int(input("Qual numero você acha que eu pensei? "))
    if number == sorteado:
        print(f"\033[32mParabéns!! Eu pensei no numero {sorteado} e você acertou!\033[m")
    else:
        print(f"\033[31mQue pena... Eu pensei no numero {sorteado} e você errou!\033[m")
if opcao == 2:
    print("A opção selecionada foi tabuada")