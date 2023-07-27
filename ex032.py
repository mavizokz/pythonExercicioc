from datetime import date
a = int(input('De um ano, lhe direi se é bissexto ou não:(Se vc quiser analisar o ano atual, digite 0) '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('É BISSEXTO!')
else:
    print('NÃO é BISSEXTO!!')

