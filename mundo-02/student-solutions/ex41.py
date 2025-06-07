# Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# 1) Até 9 anos: MIRIM
# 2) Até 14 anos: INFANTIL
# 3) Até 19 anos: JÚNIOR
# 4) Até 20 anos: SÊNIOR
# 5) Acima de 20 anos: MASTER 

print('CONFERERAÇÃO NACIONAL DE NATAÇÃO')
print('Digite sua idade para saber a categoria')

ano_atual = int(input('Ano atual: '))
ano_nascimento = int(input('Ano de Nascimento: '))

idade = ano_atual - ano_nascimento 

idade_minima = 1
idade_maxima_mirim = 9
idade_maxima_infantil = 14
idade_maxima_junior = 19
idade_maxima_senior = 20
idade_minima_master = 21

print(f'A sua idade é de {idade} anos.')

if idade >= idade_minima and idade <= idade_maxima_mirim: 
    print('Você está na categoria MIRIM')
elif idade > idade_maxima_mirim and idade <= idade_maxima_infantil: 
    print('Você está na categoria INFANTIL')
elif idade > idade_maxima_infantil and idade <= idade_maxima_junior:
    print('Você está na categoria JÚNIOR')
elif idade > idade_maxima_junior and idade <= idade_maxima_senior:
    print('Você está na categoria SÊNIOR')
elif idade >= idade_minima_master:
    print('Você está na categoria MASTER')
else:
    print('Idade inválida para as categorias disponíveis.')
    
# Fim do Desafio 41 