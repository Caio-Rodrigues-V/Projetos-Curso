"""Isso é um jogo de adivinhação de numeros."""
import random
#1. Exiba alguma mensagem de apresentação, que apresenta seu programa para o usuário
print("Bem-vindo ao jogo de adivinhação!")
print("tente avinhar um número de 1-10 ")

seu_nome = input ("Diga seu nome jogador: ")

#Looping para continuar tentando achar o numero certo
while True:
    try:
        escolha = int(input("Olá Usuário! Digite um numero de 1-10 para tentar acertar: "))
        
        

        #declarando o numero para poder gerar um numero aleatorio
        numero = random.randint(1,110)
        
        if numero == escolha:
            print("Você Acertou ",seu_nome)
            #Decisão de continuar jogando ou não!
            decisao = input("VocÊ DEseja continuar jogando?! ")
            if decisao != 's':
                break

        elif numero <= escolha:
            print("\nVocê Errou, tente um numero menor ", seu_nome)

        elif numero >= escolha:
            print("\nVocê Errou, tente um numero maior ", seu_nome)
    
    except:
        print("Digite apenas numeros")

