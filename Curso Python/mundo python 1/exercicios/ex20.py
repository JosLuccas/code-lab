# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

alunos = []

for i in range(5):
    nome = str(input("Diite o nome dos alunos: "))
    alunos.append(nome)

sorteio = random.choice(alunos)

print(f"Cachorro escolhido foi você: {sorteio}")
