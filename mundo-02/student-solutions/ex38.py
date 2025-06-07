# Desafio 38: Escreva um programa que leia dois números inteiros e os compare.
# Mostre na tela uma mensagem indicando:
# 1) O primeiro valor é maior
# 2) O segundo valor é maior
# 3) Não existe valor maior, os dois são iguais 

print('Digite dois números e eu te conto qual é o maior')

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print(f'O primeiro número é o maior! ({n1})')
elif n1 < n2:
    print(f'O segundo número é o maior!({n2})')
elif n1 == n2:
    print('Os dois números são iguais!')
else:
    print('Ocorreu um erro, tente novamente mais tarde.')
    
# Fim do Exercício 38