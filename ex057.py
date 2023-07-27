s = 0
while s != 'f' and s != 'm':
    s = str(input('Qual o seu sexo?: [M/F]')).lower().strip()
    if  s != 'f' and s != 'm':
        print('Dado inválido', end='. ')

print('Sexo registrado com sucesso!')


'''sexo=str(input('informe o seu sexo:).strip.lower
while sexo not in 'MmFf':
      sexo= str(input('Dados invalidos. Por favor, informe o sexo: ')).strip.lower
  print('Sexo registrado com sucesso')'''





