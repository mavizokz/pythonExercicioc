x=str(input('Digite uma frase: ')).strip().upper()
print('A letra -A- apareceu {} vezes'.format(x.count('A')))
print('A primeira letra -A- apareceu na posição {}'.format(x.find('A')+1))
print('A ultima letra -A- aparece na pisoçãp {}'.format(x.rfind('A')+1))
