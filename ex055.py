
maior_peso=0
menor_peso=0
for c in range (1,6):
    p = float (input (f'Peso da {c}° pessoa: '))
    if c == 1:
        maior_peso = p
        menor_peso = p

    else:
        if p>maior_peso:
            maior_peso=p
        if p<menor_peso:
            menor_peso=p

print(f'''O maior peso lido foi de {maior_peso}Kg
O menor peso lido foi de {menor_peso}Kg''')

