print('=' * 10, 'LOJAS MAVISUKA', '=' * 10)
c = float(input('Total das compras: R$'))
print('''METODO DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
mdp = int(input('Qual é a sua escolha? '))

if mdp == 1:
    desc = (c - ((10 / 100) * c))
    print('Vc terá 10% de desconto, logo irá pagar R${:.2f}'.format(desc))
elif mdp == 2:
    desc = (c - ((5 / 100) * c))
    print('Vc tera 5% de desconto, logo irá pagar R${:.2f}'.format(desc))
elif mdp == 4:
    par = int(input('Quantas parcelas? '))
    resul = c/par
    aum = (resul + ((20 / 100) * resul))
    print('''Sua compra será parcelada  em {}x de R${:.2f} O JUROS JÁ ESTÁ APLICADO
Sua compra de R${:.2f} vai custar R${:.2f}'''.format(par, aum, c, aum*10))
elif mdp == 3:
    print('O preço permanece o mesmo! R${}'.format(c))
else:
    print('ERRO')
