#: Faça um programa que leia um número qualquer
# e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
m=1
n = int(input('''Digite um número para
calcular seu Fatorial: '''))
print(f'Calculando {n}!', end=' = ')
for c in range(n, 0, -1 ):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    m = m * c
print(m)

'''n = int(input('Digite um numero: '))
c = n
f = 1
while c>0:
    print(c, end='')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print(f)'''
