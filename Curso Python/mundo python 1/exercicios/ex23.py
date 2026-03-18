# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Ex: Digite um número: 1834

# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

num = str(input("Digite um número de 0 a 9999: "))

print (f"\nSua unidade é: {num[0]}")
print (f"Sua dezena é: {num[1]}")
print (f"Sua centena é: {num[2]}")
print (f"Sua milhar é: {num[3]}")