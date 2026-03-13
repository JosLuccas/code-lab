# Faça um programa que leia a largurra e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que ca litro de tinta, pinta uma área de 2m²

altura = float(input('Qual a altura dessa parede? '))
largura = float(input('Qual a largura da parede? '))

area = altura * largura
litros = area / 2

print (f'A parede tem a dimensão de {altura}m x {largura}m e sua área é de {area}')
print (f'Para pintar essa parede, você precisará de {litros}l de tinta')