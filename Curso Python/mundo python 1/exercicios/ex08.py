# Escreva um programa que leia um valor em metros e o exiba convertido em CM e MM.

m = float(input('Digite uma distancia: '))

cm = m * 100
mm = cm * 100

print (f'A distância {m}m, é igual a: {cm}cm, {mm}mm.')