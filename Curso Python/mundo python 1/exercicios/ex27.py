# Faça um programa que leia o noem completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input("Digite seu nome completo: ")).strip()

partes = nome.split()

primeiro_nome = partes[0]
ultimo_nome = partes[-1]

print(f"Seu primeiro nome é: {primeiro_nome}")
print(f"Seu último nome é: {ultimo_nome}")
