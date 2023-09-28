import random

print("\nBem vindo ao Pedra - Papel - Tesoura! ")
print("Tente sua sorte! ")
nome = input("Digite seu nome jogador: ")

import random

#Looping para vereficar quem ganha e quem perde
while True:
    options = ["pedra", "papel", "tesoura"]
    npc = random.choice(options)

    escolha = input("Você deseja Pedra, Papel ou Tesoura? ").lower()

    if escolha == npc:
        print('Empate')
    elif escolha == 'pedra':
        if npc == 'tesoura':
            print(f'Você ganhou de {npc}', nome)
        else:
            print(f'Você perdeu para {npc}', nome)
    elif escolha == 'papel':
        if npc == 'pedra':
            print(f'Você ganhou de {npc}', nome)
        else:
            print(f'Você perdeu para {npc}', nome)
    elif escolha == 'tesoura':
        if npc == 'papel':
            print(f'Você ganhou de {npc}', nome)
        else:
            print(f'Você perdeu para {npc}', nome)
    else:
        print('Escolha inválida. Por favor, escolha entre Pedra, Papel ou Tesoura.')

    #condição para continuar jogando ou não
    play_again = input("Deseja jogar novamente? (sim/não) ").lower()
    if play_again != 'sim':
        break

    

