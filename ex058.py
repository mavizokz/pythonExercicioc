import random
print('''Sou seu computador
Acabei de pensar em um número entre 0 e 10.
Será que voçê consegue adivinhar qual foi?''')
nn = 0
nm = 0
s = 0
p = 0
c = random.randint(0,10)
while p != c:
    p = int(input('Qual o seu palpite? '))
    if p>c:
        print('Menor que isso... Tente mais uma vez!')
        nn += 1
    if p<c:
        print('Maior que isso... Tente mais uma vez!')
        nm += 1
    if p==c:
        s += 1
print(f'''\033[34mAcertou!\033[m
Com {s+nn+nm} tentativa(s). Parabéns!''')