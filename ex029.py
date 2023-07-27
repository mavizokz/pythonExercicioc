v= float(input('Qual a velocidade que estava na via?: Km/h '))
if v > 80:
    print(
    '''\033[31mLevou multa ruizão\033[m
E vai ter que pagar R$ {}'''.format((v-80)*7))
else:
    print('\033[32mPrudente!!')
