nome = str(input('Qual o seu nome? '))
if nome == 'Maria':
    print('Nome bonito!')
elif nome == 'Pedro' or nome == 'Gustavo':
    print('Seu nome é bem popular!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}'.format(nome))
