a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificar quem é o menor
if a<b and a<c:
    menor=a
if b<a and b<a:
    menor=b
if c<a and c<b:
    menor=c
# Verificar que é o maior
if  a>b and a>c:
    maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

print('''O MENOR valor é \033[31m{}\033[m.
E o MAIOR é \033[31m{}\033[m.'''.format(menor, maior))
