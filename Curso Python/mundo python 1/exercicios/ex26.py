# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A".

# Em que posição ela aparece a primeira vez.

# Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).upper()

contador = frase.count("A")
primeira_vez = frase.find("A") + 1
ultima_vez = frase.rfind("A") + 1

print(f"Nessa frase a letra A apareceu: {contador} vezes.")
print(f"A primeira vez aparece na posição: {primeira_vez}")
print(f"A última vez aparece na posição: {ultima_vez}")
