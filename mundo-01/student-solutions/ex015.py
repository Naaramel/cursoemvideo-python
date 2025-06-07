# Exercício 15: Escreva um programa que calcule o preco a pagar de um carro alugado.
# Calcule a quantidade de KM percorridos e a quantidade de dias pelos quais ele foi alugado.
# O carro custa R$60,00 por dia e R$0,15 por KM rodado

km_percorridos = float(input("Digite a quantidade de KM percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias alugados: "))

preco = (dias_alugados * 60) + (km_percorridos * 0.15)

print(f"O preço a pagar é R$ {preco:.2f}.") 

# Fim do exercício 15