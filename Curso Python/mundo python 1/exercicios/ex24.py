# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input("Digite uma cidade: "))

pesquisa = cidade.split()[0]

if pesquisa == "Santo":
    {
        print ("Essa cidade começa com Santo no nome.")
    }
else:
    {
        print ("Essa cidade não começa com Santo no nome.")
    }