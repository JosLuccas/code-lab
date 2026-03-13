# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo.

import math

a = float(input("Digite o Angulo: "))

a = math.radians(a)

s = math.sin(a)
c = math.cos(a)
t = math.tan(a)

print(
    f"Para o Angulo escolhido, temos o Seno {s:.2f}, Coseno {c:.2f} e a Tangete {t:.2f}"
)
