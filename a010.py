#basicamente fiz um programa que me desse o resultado de se tivesse maria no nome
# ele daria o print de nome bonito, antes so aceitava se eu escrevesse apenas maria
#agora maria pode ser um nome composto qeu vai da bom

n = str(input('Qual o seu nome?: ')).strip().upper()
x = n.split()
if x [0]== 'MARIA':
    print('Que nome bonito')
print('Bom dia, {}'.format(n))
