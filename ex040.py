print('\033[35m-\033[m' * 22)
print('\033[34mCALCULADORA DE MÉDIAS\033[m')
print('\033[35m-\033[m' * 22)

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print('Sua média é {}'.format(media))

if media < 5.0:
    print('\033[31mREPROVADO\033[m')

elif 7 > media >= 5:
    print('\033[33mRECUPERAÇÃO\033[m')

elif media >= 7.0:
    print('\033[36mAPROVADO\033[m')
