# Crie um programa qu eleia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas

# o nome com todas letras minúsculas

# Quantas letras ao todo (sem considerar espaços)

# Quantas letras tem o primeiro nome

nome = str(input("Diga seu nome completo: "))

maiusculo = nome.upper()
minusculo = nome.lower()
sem_espaco = nome.replace(" ", "")
contador = len(sem_espaco)
primeiro_nome = nome.split()[0]

print(f"\nAssim fica seu nome todo Maiúsculo: {maiusculo}")
print(f"Assim fica seu nome todo Minúsculo: {minusculo}")
print(f"Seu nome tem {contador} letras ao todo.")
print(f"Seu primeiro nome tem {len(primeiro_nome)} letras.")