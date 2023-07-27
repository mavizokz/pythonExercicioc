s = float(input('Qual é o seu sálario?: R$'))
if s > 1250.00:
    r=(s+((10/100)*s))
    print('Vc tera uma aumento de 10%, logo vai passar a receber R${:.2f} agora'.format(r))
if s < 1250.00:
    r=(s+((15/100)*s))
    print('Vc tera um aumento de 15%, logo vai passar a receber R${:.2f} agora'.format(r))
