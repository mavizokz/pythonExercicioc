total = 0
caro = 0
b = 0
mc = 0
vulgo = 0
cont = 0

print('+-'*14)
print('     LOJA SUPER BARATÃO     ')
print('+-'*14)
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        caro += 1

    if cont == 1:
        b = preço
        vulgo=nome
    else:
        if preço < b:
            b = preço
            vulgo=nome

    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar?: [S/N] ')).upper()
    if r == 'N':
        break



print(f'O total da compra foi R${total :.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {vulgo} que custa R${b} ')


