km = float(input('Quantos kms vc percorreu com o carro?: '))
dias = int(input('E quanots dias ele ficou com vc?: '))

f = (km * 0.15)
f2 = (dias * 60)
R = f + f2

print('O total a pagar é de R${:.2f}'.format(R))

