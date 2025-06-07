# Desafio 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e a condição de pagamento:
# 1) À vista em dinheiro ou cheque: 10% de desconto
# 2) À vista no cartão: 5% de desconto
# 3) Até 2x no cartão: Preço normal
# 4) 3x ou mais no cartão: 20% de juros

print('Calculadora de Preço de Produto.\nDigite o preço do produto e a forma de pagamento para calcular o valor final.') 

preco_produto = float(input('Digite o preço do produto: R$'))
print('Escolha a forma de pagamento:')
print('1) À vista em dinheiro ou cheque')
print('2) À vista no cartão')
print('3) Até 2x no cartão')
print('4) 3x ou mais no cartão')

opcao_pagamento = int(input('Digite a opção desejada (1/2/3/4): '))

if opcao_pagamento == 1:
    preco_final = preco_produto * 0.9
    print(f'O valor final a ser pago é R${preco_final:.2f} (10% de desconto)')
elif opcao_pagamento == 2:
    preco_final = preco_produto * 0.95
    print(f'O valor final a ser pago é R${preco_final:.2f} (5% de desconto)')
elif opcao_pagamento == 3:
    print(f'O valor a ser pago é R${preco_produto:.2f} (sem desconto)')
elif opcao_pagamento == 4:
    preco_final = preco_produto * 1.2
    print(f'O valor final a ser pago é R${preco_final:.2f} (20% de juros)')
else:
    print('Opção inválida! Por favor, escolha uma opção válida.')
      
# Fim do desafio 44.