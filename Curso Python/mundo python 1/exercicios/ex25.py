# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input("Digite seu nome completo: ")).upper()

verificador = nome.find("SILVA")

if verificador == -1:
    print("Seu nome não tem Silva.")
else:
    print("Seu nome tem Silva.")
