

preço=float(input('Qual o preço do produto? R$'))
#descreal = (5 / 100) * prod
#descporc = (prod - descreal)
#print('O produto que custa R${}, na promoção de 5% vai custar R${:.2f}'.format(prod, descporc))
novo = (preço-((5/100)*preço))
print('O produto que custa R${}, na promoção de 5% vai custar R${:.2f}'.format(preço, novo))

