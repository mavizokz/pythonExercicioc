'''import random

print ('Qual aluno, entre 4 alunos, devo escolher? Augusto(1), Bernardo(2), Guilherme(3) e Maria(4)  ')
print (random.randint(1, 4))'''
'''import random

a1=str(input('Primeiro aluno: '))
a2=str(input('Segundo aluno: '))
a3=str(input('Terceiro aluno: '))
a4=str(input('Quarto aluno: '))
seq=
print('O aluno escolhido foi {}'.format(random.Random))'''

from random import choice
a1=str(input('Primeiro aluno: '))
a2=str(input('Segundo aluno: '))
a3=str(input('Terceiro aluno: '))
a4=str(input('Quarto aluno: '))
seq = (a1 , a2, a3, a4 )

print('O nome escolhido foi:', choice(seq))
