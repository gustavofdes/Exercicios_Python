from time import sleep

print("-="*20)
print("Analisador de Triangulos")
print("-="*20)
sleep(0.5)

r1 = float(input("Valor do primeiro segmento: "))
r2 = float(input("Valor do segundo segmento: "))
r3 = float(input("Valor do terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print("Esses segmentos \033[32mPODEM \033[mformar um triangulo")
    if r1 == r2 and r2 == r3:
        print("O triangulo formado sera um \033[36mEquilatero\033[m")
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("O triangulo formado sera um \033[35mIsóceles\033[m")
    else:
        print("O triangulo formado sera um \033[34mEscaleno\033[m")
else:
    print("Esses segmentos \033[31mNÃO PODEM \033[mformar um triangulo")
