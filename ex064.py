s=0
n=0
d=0


while n != 999:
    n=int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        s+=n
        d+=1
print(f'Vc digitou {d} números e a soma entre eles é {s} ')
