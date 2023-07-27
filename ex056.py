#Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o
# nome do homem mais velho e quantas mulheres têm menos de 20 anos.
s = 0
hv = 0
nh = 0
mn = 0
for c in range(1,5):
    print(f'----{c}° PESSOA----')
    n = str(input('Nome:')).upper()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper()


    if idade > 0:
        s = s + idade

    if sexo == 'M':
        if idade>hv:
            hv=idade
            hn=n

    if sexo == 'F':
        if idade <= 20:
            mn = mn+1


print('A média de idade do grupo é de',s/4,'anos')
print(f'O homem mais velhor tem {hv} anos e se chama {hn}')
print(f'Ao todo são {mn} mulheres com menos de 20 anos')
