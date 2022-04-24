print("\033[34m-="*20)
print("Analisador de Triangulos")
print("-="*20)
r1 = float(input("\033[mPrimeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("Esses segmentos \033[32mPODEM \033[mformar um tringulo")
else:
    print("Esses segmentos \033[31mNÃO PODEM \033[mformar um tringulo")
