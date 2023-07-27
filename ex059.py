n1 =  int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
r = 0
n1 = n1
n2 = n2
while r != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    r=int(input('Qual a sua opção? '))

    if r == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')

    if r == 2:
        print(f'A multiplicação de {n1} x {n2} é {n1*n2}')

    if r == 3:
        if  n1>n2:
            print(f'O {n1} é o maior númeor')
        if n1<n2:
            print(f'O {n2} é o maior número')
        else:
            print(f'Os valores são iguais! Logo {n1} é o maior e menor número')

    if r == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    if r == 5:
        print('Obrigada por jogar!')
        break
    print('-==-'*9)