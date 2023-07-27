r = 'SsNn'
sexo = 'FfMm'
i = 0
s = 0
n = 0
while True:
    print('-'*28)
    print('   CADASTRE UMA PESSOA  ')
    print('-' * 28)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'FfMm':
        sexo = str(input('Sexo: [M/F] ')).upper()
    print('-' * 20)
    r = str(input('Que continuar? [S/N] ')).upper()

    while r not in 'SsNn':
        r = str(input('Que continuar? [S/N] ')).upper()

    if idade >= 18:
        i += 1
    if sexo == 'M':
        s += 1
    if sexo == 'F' and idade < 20:
        n += 1
    if r == 'N':
        break
print('=====FIM DO PROGRAMA=====')
print(f'O total de pessoas com mais de 18 anos : {i}')
print(f'Tem o total de {s} homem(s)')
print(f'E {n} mulher(es) com menos de 20 anos')