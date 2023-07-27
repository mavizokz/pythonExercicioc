x=str(input('Digite seu nome completo: ')).strip().split()
print('''Muito prazer em te conhecer,
Seu primeiro nome é {}
Seu ultimo nome é {}'''.format(x[0], x[-1]))
