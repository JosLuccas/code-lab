# Manipulação de texto.

# Para o python toda cadeia de texto está entre aspas simples ou aspas dupla.

# str ou string

# Fatiamento:

# string[inicio:fim:passo]

# Inicio → posição onde começa
# Fim → posição onde termina (não inclui esse índice)
# Passo → de quantos em quantos caracteres ele anda

# frase = 'Curso em Vídeo Python'

# print (frase[9]) -> mostra a letra de acordo com o índice selecionado

# Outras maneira de fatiamento:
# frase = 'Curso em Vídeo Python'

# print (frase[9:14]) -> mostra do índice 9 até 13 (o 14 não entra).
# print (frase[9:14:2]) -> mostra de 2 em 2
# print (frase[:5]) -> mostra do começo até 4
# print (frase[15:]) -> mostra do índice até o final
# print (frase[9::3]) -> mostra do ídice até o final de 3 em 3

# Análise:

# len()
# Length - Comprimento
# Conta quantos caracteres existem em uma string.

# .count()
# Conta quantas vezes um caractere ou palavra aparece na string.

# .find()
# Mostra a posição (índice) da primeira vez que algo aparece na string.

# Transformação:

# .replace()
# Substitui uma palavra ou caractere por outro dentro da string.

# .upper()
# Transforma todas as letras da string em maiúsculas.

# .lower()
# Transforma todas as letras da string em minúsculas.

# .capitalize()
# Deixa apenas a primeira letra da string maiúscula e o resto minúsculo.

# .title()
# Coloca a primeira letra de cada palavra em maiúscula.

# .strip()
# Remove os espaços vazios do começo e do final da string.

# .rstrip()
# Remove os espaços vazios apenas do final da string.

# .lstrip()
# Remove os espaços vazios apenas do começo da string.

# Exemplos prático:

frase = "Curso em Vídeo Python"
frase_alternativa = "   Aprenda Python   "
print(f"Frase para exemplo: {frase}")

print("\nFatiamentos de strings:")

print("\n" + frase[9])
print(frase[9:14])
print(frase[9:14:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print("\nAnálise de strings:")

print("\n" + f"Essa frase tem {len(frase)} caracteres")
print(f'Essa frase repetiu o caracter "o" {frase.count('o')} vezes')
print(f'Na frase, a palavra "Python" começa no índice: {frase.find('Python')}')

print("\nTransformção de strings:")

print("\n" + frase.replace("Python", "PHP"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase_alternativa.strip())
print(frase_alternativa.rstrip())
print(frase_alternativa.lstrip())