
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
    print("A opção selecionada foi \033[4;36mJogo de Adivinhação\033[m !")
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
    print("A opção selecionada foi \033[4;36mTabuada\033[m !")
    n = int(input("Digite um numero para saber sua tabuada: "))
    time.sleep(1)
    print("--"*20)
    time.sleep(1)
    print(f"{n} x 1 = {n*1}")
    time.sleep(0.2)
    print(f"{n} x 2 = {n*2}")
    time.sleep(0.2)
    print(f"{n} x 3 = {n*3}")
    time.sleep(0.2)
    print(f"{n} x 4 = {n*4}")
    time.sleep(0.2)
    print(f"{n} x 5 = {n*5}")
    time.sleep(0.2)
    print(f"{n} x 6 = {n*6}")
    time.sleep(0.2)
    print(f"{n} x 7 = {n*7}")
    time.sleep(0.2)
    print(f"{n} x 8 = {n*8}")
    time.sleep(0.2)
    print(f"{n} x 9 = {n*9}")
    time.sleep(0.2)
    print(f"{n} x 10 = {n*10}")

if opcao == 3:
    print("a opção selecionada foi \033[4;36mVerificador de Multas\033[m !")
    time.sleep(0.5)
    vm = 80
    v = float(input("Digite a velocidade de seu carro para saber se tomou multa ou não: "))
    print("Processando...")
    time.sleep(1)
    if v > vm:
        multa = v - vm
        print(f"\033[31mVocê passou o limite de velocidade de {vm}Km/h e recebeu uma multa\033[m")
        valor_multa = float(multa * 7)
        print(f"Você recebeu uma multa de \033[32mR${valor_multa:.2f}\033[m por passar \033[31m{multa:.0f}Km/h\033[m do limite permitido")
    else:
        print(f"\033[32mVocê estava dentro do limite de velocidade e não foi multado\033[m")
    print("Obrigado por usar nosso PROGRAMA!")
