a1 = int(input('Primeiro termo da P.A.: '))
r = int(input('A razão da P.A.: '))
c = 1
p = 10
total = 0
termo= a1#¹
while p != 0:
    total=total+p
    while c <= total:
        print(termo, end=' ➡ ')# (especiquei ali encima ¹)como ele ja tem o resultado do termo, vai ser o primiro elemento que ele ira colocar na progreção
        termo = a1 + (c * r)
        c += 1 #aqui ele vai somando os 'c' para que ele faça a progressao(em tese é para aumentar a posição do termo)
    print('PAUSA')
    p = int(input('Quantos termos a mais vc gostaria de colocar?'))
print('FIM')
print(f'O Programa foi finalizado com o total de {total} termos')




