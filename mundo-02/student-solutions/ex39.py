# Desafio 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('Bem-vindo ao site de alistamento Militar')
print('Digite o ano atual e o ano de alistamento para saber se você já pode se alistar.')

ano_atual = int(input('Ano atual: '))
ano_nascimento = int(input('Ano de Nascimento: '))

idade = ano_atual - ano_nascimento 

idade_minima_alistamento = 18
idade_maxima_alistamento = 25

print(f'A sua idade é de {idade} anos.')

if idade >= idade_minima_alistamento and idade <= idade_maxima_alistamento: 
    print('Você está dentro da idade permitida para o alistamento Militar.')
elif idade < idade_minima_alistamento:
    print(f'Você não possui a idade mínima para se alistar. \nFaltam {idade_minima_alistamento - idade} anos para você completar a idade mínima necessária para o alistamento militar.')
elif idade > idade_maxima_alistamento: 
    print(f'Você não pode mais se alistar!\nA idade máxima de alistamento é {idade_maxima_alistamento}.\nVocê têm {idade - idade_maxima_alistamento} a mais da idade máxima de alistamento.') 
else:
    print('Ocorreu um erro. Tente novamente mais tarde.')
    
# Fim do desafio 39