# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qaul o salário do funcionário? R$'))

aumento = salario * 0.15
salario_final = salario + aumento

print (f'Com o aumento de 15%, o novo salário ficará de R$ {salario_final}')