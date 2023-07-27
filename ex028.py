import random
import time
import colorsys
print('\033[1;35m-=-\033[m' *20)
print('\033[1;36mVou pensar em um numero entre 0 a 5, tente advinhar se for capaz!\033[m')
print('\033[1;35m-=-\033[m' *20)
r = int(input('Que numero vc acha que é?: '))
n2 = random.randint(0,5)
print('\033[1;32mPROCESSANDO. . .\033[m')
time.sleep(2)
if r == n2:
    print('Cagou muito em rei, acertou!!!')
else:
    print('Ruizão, o número era {}'.format(n2))
