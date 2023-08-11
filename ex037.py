num = int (input('De qualquer valor inteiro: '))
print('''Escolha base de conversão será: 
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')

modo = int (input('Sua opção: '))

if modo == 1:
    binario = bin(num)[2:]
    print(binario)
elif modo == 2:
    octal = oct(num)[2:]
    print(octal)
elif modo == 3:
    hexa = hex(num)[2:]
    print(hexa)
else:
    print('Tente novamente')
