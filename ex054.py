import datetime
#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
s=0
n=0
for c in range (1,8):
    ano=int(input(f'Em que ano a {c}° pessoa nasceu?: '))
    idade= datetime.date.today().year - ano
    if idade >= 21:
        s = s + 1



    elif idade <21:
        n = n + 1

print(f'{n} pessoas são MENOR de idade')
print(f'{s} pessoas são MAIOR de idade')


