# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

cat1 = float(input("Digite o cateto 1: "))
cat2 = float(input("Digite o cateto 2: "))

hipo = math.hypot(cat1, cat2)

print(f"O valor da hipotenusa do triângulo é: {hipo}")
