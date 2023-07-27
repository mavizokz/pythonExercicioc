import time
import datetime
ano = int(input('Ano de nascimento: '))
idade =datetime.date.today().year - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, datetime.date.today().year))
print('\033[32mP R O C E S S A N D O. . .\033[m')
time.sleep(2)
if idade<18:
    print('''Faltam {} anos para o seu alistamento.
Que será em {}!!'''.format(18-idade, ano+18))
elif idade==18:
    print('''Estamos no ano do seu alistamento,
BOA SORTE!!''')
else:
    print('''Já se passaram {} anos do seu alistamento,
O ano do seu alistamento foi em {}!!'''.format(idade-18, ano+18))

