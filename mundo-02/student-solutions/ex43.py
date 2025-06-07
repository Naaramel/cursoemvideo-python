# Desafio 43: Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida

print('Calculadora de IMC.\nDigite seu peso e a sua altura para calcular o seu IMC.')

peso = float(input('Digite o seu peso em quilogramas (kg):'))
altura = float(input('Digite sua altura em metros (m):'))

imc_usuario = peso / (altura * altura)

minimo_imc_pesoideal = 18.5
minimo_imc_sobrepeso = 25
minimo_imc_obesidade = 30
minimo_imc_obesidade_morbida = 40

print(f'Seu IMC é {imc_usuario:.1f}.')

if imc_usuario < minimo_imc_pesoideal:
    print(f'Abaixo do peso')
elif imc_usuario >= minimo_imc_pesoideal and imc_usuario < minimo_imc_sobrepeso:
    print(f'Peso ideal')
elif imc_usuario >= minimo_imc_sobrepeso and imc_usuario < minimo_imc_obesidade:
    print(f'Sobrepeso')
elif imc_usuario >= minimo_imc_obesidade and imc_usuario < minimo_imc_obesidade_morbida:
    print(f'Obesidade')
elif imc_usuario >= minimo_imc_obesidade_morbida:
    print(f'Obesidade mórbida')
else:
    print(f'Erro ao calcular o IMC. Verifique os valores digitados.')
    
# Fim do desafio 43.