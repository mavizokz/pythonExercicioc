p=float(input('Qual é a distancia da sua viagem em Km? KM '))

if p <= 200.0 :
    print('A sua passagem vai custar R${:.1f}'.format(p*0.50))
else:
    print('A sua passagem vai custar R$ {:.1f}'.format(p*0.45))
