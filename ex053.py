f=(input('''Digite uma frase 
e te direi se ela é um palíndromo ou não: ''')).upper()

frase_sem_espacos = f.replace(' ', '')

print(f'O inverso de {frase_sem_espacos} é {frase_sem_espacos[::-1]}')

if frase_sem_espacos==frase_sem_espacos[::-1]:
    print('é palídromo')
else:
    print('Não é Palíndromo')


