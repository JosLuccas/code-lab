
#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite mais um número: '))
#s = n1 + n2

#print ('A soma vale:', s)
#print ('A soma vele: {}'.format{s}) Não se usa mais essa maneira do .format
#print (f'A soma vale: {s}') Maneira mais atual do .format

#int = Número inteiro Ex: 7 -4 0
#float = Número real Ex: 4.5 7.0 3.14
#bool = Booleano Ex: True | False
#str = Texto Ex: 'Oi' '5' ''

#Juntar duas string se chama de concatenação
#Ex:
#texto1 = str(input('Digite uma palavra: '))
#texto2 = str(input('Digite outra palavra: '))

#juncao = texto1 + texto2

#Desafio Aula 02:

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

s = n1 + n2

print (f'A soma entre {n1} e {n2}, gera o resultado de: {s}')

a = input('Digite qualquer coisa: ')
print(a.isalnum(), a.isalpha(), a.isascii(), a.isdecimal(), a.isdigit(), a.isidentifier(), a.islower(), a.isnumeric(), a.isprintable(), a.isspace(), a.istitle(), a.isupper())