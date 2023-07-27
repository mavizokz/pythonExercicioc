import random

print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")

'''jogadas = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Escolha sua jogada (pedra, papel ou tesoura): ")
    computador = random.choice(jogadas)

    print(f"\nVocê escolheu {jogador} e o computador escolheu {computador}.")

    if jogador == computador:
        print("\033[33mEmpate!\033[m")

    elif jogador == "pedra":
        if computador == "papel":
            print("Você perdeu!")
        else:
            print("Você ganhou!")

    elif jogador == "papel":
        if computador == "tesoura":
            print("Você perdeu!")
        else:
            print("Você ganhou!")

    elif jogador == "tesoura":
        if computador == "pedra":
            print("Você perdeu!")
        else:
            print("Você ganhou!")

    else:
        print("Escolha inválida! Tente novamente.")
        continue

    jogar_novamente = input("Quer jogar novamente? (s/n): ")
    if jogar_novamente.lower() != "s":
        break

print("Obrigado por jogar!")'''

op = ['pedra', 'papel', 'tesoura']
comp = random.choice(op)
jogador = str(input('''Escolha oq vc vai jogar (pedra, papel ou tesoura): ''')).strip().lower()

print(f'\nO computador escolheu {comp} e você escolheu {jogador}!')

if comp == jogador:
    print('\033[33mEmpate!\033[m')

elif comp == 'tesoura':
    if jogador == 'pedra':
        print('VC ganhou')
    else:
        print('VC perdeu')

elif comp == 'pedra':
    if jogador == 'papel':
        print('VC ganhou')
    else:
        print('VC perdeu')

elif comp == 'papel':
    if jogador == 'tesoura':
        print('VC ganhou')
    else:
        print('VC perdeu')
