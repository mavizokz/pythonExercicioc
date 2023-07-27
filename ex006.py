import math

x= int (input('De um número:'))
d= x*2
t= x*3
#r4= pow(x,(1/2))
#r4= x**(1/2)
r4= math.sqrt(x)
print ('O dobro de {} é {}, o triplo é {} \nE a sua raiz quadrada é {:.2f}'.format(x,d, t, r4))
