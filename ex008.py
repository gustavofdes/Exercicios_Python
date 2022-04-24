#Programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = float(input("Quantos metros? "))

cm = m * 100
mm = m * 1000

print(f"{m}m é igual a {cm}cm ")
print(f"{m}m é igual a {mm}mm")