n = 0
c = 1
while True:
    n = int(input('Quer ver a tabuada de que valor?: '))
    print('-' * 20)
    if n < 0:
        break
    while c <= 10:
        m = n * c
        print( n,'x', c, '=', m)
        c += 1
    c -= 10
print('ACABOU')