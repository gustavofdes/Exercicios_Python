nome = str(input("Digite o nome de sua cidade: ")).strip()
cidade = str(input("Primeiro nome: ")).strip().upper()
dividido = nome.upper().split()
r = cidade in dividido[0]
print(f"Sua cidade ({nome.title()}) começa com {cidade.title()}? {r}")

#Adicionei a opção de adicionar a primeira palavra ao inves de Santo
