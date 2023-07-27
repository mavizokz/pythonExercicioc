n = int(input('De um número: '))
count=0
for c in range(1, n + 1):
    d1 = n / c

    if d1==n and d1==1:
        print('\033[35m',c,'\033[m', end='')
        count = count + 1

    elif n%c==0:
        print('\033[35m',c,'\033[m', end='')
        count = count + 1

    else:
        print('\033[36m',c,'\033[m', end='')


print(f'''\n➡O número {n} foi divisível {count} vezes (números em roxo)''')
if count==2:
    print('Por isso É PRIMO')
else:
    print('E por isso NÃO É PRIMO')
