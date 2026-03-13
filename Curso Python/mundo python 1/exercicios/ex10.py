# Crie um programa que leia quanto dinheiro uma pessao tem na carteira e mostre quantos dólares ela pode comprar

# OBS: Cotaçao 2026, R$ 1 = U$ 5,24

carteira = float(input('Quanto você tem na carteira? '))

dolar = carteira / 5.24

print (f'Com R${carteira}, dá para comprar U${dolar}')