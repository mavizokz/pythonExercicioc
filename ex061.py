'''a1 = int(input('Primeiro termo da P.A.: '))
r = int(input('A razão da P.A.: '))
termo=a1
c=1
while c<=10:
    print(termo, end=' ➡ ')
    termo+=r
    c+=1
print('FIM')'''



a1 = int(input('Primeiro termo da P.A.: '))
r = int(input('A razão da P.A.: '))
c = 1
print(a1, end=' ➡ ')
while c < 10:
    termo = a1 + (c * r)
    c += 1
    print(termo, end=' ➡ ')
print('FIM')



