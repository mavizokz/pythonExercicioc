s = 0
#fazer repetir 6 vezes
for c in range(1, 7):
    n = int(input(f'De o {c}º valor: '))
    if n%2==0:#condiçao para ser par
       s+=n #soma de todos os valores
print(f'A soma de todos os numeros de pares é {s}')



