print('-'*23)
print('Sequencia de Fibonicci')
print('-'*23)
n = int(input('Quantos números vc quer que apareça na sequencia?'))
n1=0
n2=1
print(n1,'➡',n2, end=' ➡ ')
c=3
while c <= n:
    n3=n1+n2
    print(n3,end=' ➡ ')
    n1=n2
    n2=n3
    c+=1
print('FIM')
