r = 'SsNn'
s = 0
todos = 0
mv = 0
nv = 0
while r not in 'Nn':
    n = int(input('Digite um número: '))
    todos += n
    s += 1
    r = str(input('Quer continuar? [S/N] '))
    if n==1:
        mv = n
        nv = n
    else:
        if n > mv:
            mv = n
        else:
            nv = n
m = todos/s
print('A média entre todos os valores é {:.2f}'.format(m))
print(f'O maior valor foi {mv} e o menor foi {nv}')
