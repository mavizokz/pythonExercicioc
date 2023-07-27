a1 = int(input('Primeiro termo da P.A.: '))
r = int(input('A razão da P.A.: '))
print(a1, end=' ➡ ')
for c in range(1, 10):
    termo = a1 + (c * r)
    print(termo, end=' ➡ ')
print('FIM')

