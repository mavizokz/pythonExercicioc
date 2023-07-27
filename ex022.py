nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiusculo fica assim,  {}'.format(nome.upper()))
print('Seu nomne em minusculo fica assim,   {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome.replace(' ', ''))))
dividido= nome.split()
print('{} possui {} letras'.format(dividido[0], len(dividido[0])))

