nome = str(input("Digite seu nome inteiro: ")).strip()

print(f"O seu nome com todas as letras maisculas: {nome.upper()}")
print(f"O seu nome com todas as letras em minusculas: {nome.lower()}")

divido = nome.split()
letras = "".join(divido) #ajunta as palavras separadas pelo split
print(f"Seu nome contem: {len(letras)} letras")
print(len(nome) - nome.count(" ")) #outro jeito mais facil de fazer o comando acima

print(f"Seu primeiro nome ({divido[0]}) contem: {len(divido[0])} letras")
