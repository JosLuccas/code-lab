# Trabalhando com Módulos

# Importações de bibliotecas

# Para quando quero algo geral, eu importo a biblioteca toda usando:
# import math

# numero = int(input('Digite um número: '))
# raiz_quadrada = math.sqrt(numero)

# print (f'A raiz quadrada de {numero} é: {raiz_quadrada}')

# Para quando quero algo mais especifico sem importar a biblioteca toda uso:
# from math import sqrt

# numero = int(input('Digite um número: '))
# raiz_quadrada = sqrt(numero)

# print (f'A raiz quadrada de {numero} é: {raiz_quadrada}')

# Simples, menos funçoes e leve:\
''''
from math import sqrt

numero = int(input('Digite um número: '))
raiz_quadrada = sqrt(numero)

print (f'A raiz quadrada de {numero} é: {raiz_quadrada}')

# Geral, mais funçoes e pesado:

import math

num = int(input('\nDigite um número: '))
raiz = math.sqrt(num)

print (f'A raiz quadrada de {num} é: {math.ceil(raiz)}')
'''

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.


# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo.


# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.


# O mesmo professor do desagio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.