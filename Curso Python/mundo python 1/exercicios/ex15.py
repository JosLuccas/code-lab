# Escreva um programa que pergunte a quantiodade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado, Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodados.

dia = int(input('Quantos dias o carro rodou? '))
km = float(input('Quatnos Km o caro andou? '))

valor_dia = dia * 60
valor_km = km * 0.15

valor_final = valor_dia + valor_km

print (f'O valor a ser pago é de: R${valor_final:.2f}')