# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor_total = float(input('Pagando a vista tem um desconto de 5%, qual o valor do produto? R$'))

desconto = valor_total * 5 / 100
valor_final = valor_total - desconto

print (f'Aplicado o descoto de 5%, o valor final do produto, ficou: R${valor_final:.2f}')