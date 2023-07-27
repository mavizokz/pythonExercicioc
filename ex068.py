from random import randint
print('=='*13)
print('VAMOS JOGAR IMPAR OU PAR')
print('=='*13)

j = 0
r = 0
w = 0

while True:
    j = int(input('Digite um valor: '))
    e = str(input('Par ou Ímpar? [P/I] ')).strip().upper() [0]
    num = randint (1,10)
    soma = j + num
    print('==' * 27)
    if soma % 2 != 0:
        r = 'IMPAR'
    else:
        r = 'PAR'
    print(f'Voce jogou {j} e o computador {num}. O total deu {soma}[{r}]')
    print('==' * 27)
    if e == r[0]:
        print('\033[36mVOCE GANHOU!\033[m')
        w += 1
    elif e != r[0]:
        print('\033[31mVOCE PERDEU!\033[m')
        break
print('==' * 20)
print(f'\033[31mGAME OVER!\033[m Voce ganhou {w} vezes')