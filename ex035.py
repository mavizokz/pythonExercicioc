import time
print('\033[35m -=- \033[m'*20)
print(' Analisador de Triângulos')
print('\033[35m -=- \033[m'*20)

a = float(input('Priemiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('\033[32mPROCESSANDO...\033[m')
time.sleep(2)
if a + b > c and a + c > b and c + b > a:
    print('\033[34mDá\033[m para formar um triângulo!!')
else:
    print('\033[31mNão\033[m da para formar um triângulo!!')





