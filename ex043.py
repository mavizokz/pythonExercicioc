peso = float(input('Qual é o seu peso? (Kg) '))
alt = float(input('Qual é a sua altura? (m) '))

imc= peso/(alt**2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Vc está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Vc está no PESO IDEAL!')
elif imc >= 25 and imc <30:
    print('Vc está no SOBREPESO!')
elif imc>=30 and imc < 40:
    print('Vc está em OBESIDADE!')
elif imc>=40:
    print('Vc está em estado de OBESIDADE MORBIDA!')