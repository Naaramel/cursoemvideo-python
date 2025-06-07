# Exercício 09: Faça um programa que leia um número inteiro qualquer e mostre na sua tabuada.

numero = int(input("Digite um número inteiro: "))

print(f"Tabuada do {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    
# Fim do exercício 09
