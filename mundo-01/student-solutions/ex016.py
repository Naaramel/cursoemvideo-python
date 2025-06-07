# Exercício 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# exemplo: entrada: 6.345 ... Saida: 6

import math

numero = float(input("Digite um número real: "))

print(f"A porção inteira de {numero} é {math.trunc(numero)}.") 

# Fim do exercício 16
# O módulo math é utilizado para truncar o número real, ou seja, remover a parte decimal.
 