import time
print('\033[35m -=- \033[m'*5)
print(' Analisador de Triângulos')
print('\033[35m -=- \033[m'*5)

a = float(input('Priemiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('\033[32mPROCESSANDO...\033[m')
time.sleep(2)
if a + b > c and a + c > b and c + b > a:
    print('\033[34mDá\033[m para formar um triângulo', end='')
   #A igualdade é inclusiva, logo se B é igual a A que tbm é igual a C,
    #logo concluo que A tbm é igual a C, sem precisar fazer a comparação
    if a==b and b==c:
        print('EQUILATERO')
    #A diferença nao é assim, se b for diferente de A que tbm é diferentre de c,
    #eu nunca que vou saber se A é diferente ou igual a C KSKSKSKSKSKKS
    elif a != b and b != c and c != a:
        print('ESCALENO')
    else:
        print('ISÓCELES')

else:
    print('\033[31mNão\033[m da para formar um triângulo!!')