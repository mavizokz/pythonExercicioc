# print('Augusto', (1), 'Bernardo', (2), 'Guilherme', (3), 'Maria', (4))
# print('a ordemo dos alunos será'.sample(Augusto, Bernardo, Guilherme, Maria  k=len(4)))
from random import choice

import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
mylist = [a1, a2, a3, a4]
random.shuffle(mylist)
print('A ordem da apresentação é:\n{}'.format(mylist))
#print(mylist)
