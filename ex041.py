import datetime
print('\033[35m-\033[m'*31)
print('\033[34mConfederação Nacial de Natação\033[m')
print('\033[35m-\033[m'*31)

ano = int(input('Qual o ano do seu nascimento?: '))
idade = datetime.date.today().year - ano
print('Você tem {} anos, logo se encaixa na'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade<= 19:
    print('Categoria JÚNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
elif idade > 25:
    print('Categoria MASTER')

