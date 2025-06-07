# Exercício 23: - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. 
# Ex: Número 1834 = Unidade: 4 | Dezena: 3 | Centena: 8 | Milhar: 1

numero = int(input("Digite um número de 0 a 9999: "))

print("Analisando o número...")
print(f"Unidade: {numero % 10}")
print(f"Dezena: {(numero // 10) % 10}")
print(f"Centena: {(numero // 100) % 10}")
print(f"Milhar: {numero // 1000}")

# Fim do exercício 23