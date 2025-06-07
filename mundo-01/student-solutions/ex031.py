# Exercício 31: Desenvolva um programa que calcule o preço de uma passagem
# 1) Pergunte a distância de uma viagem em km.
# Preço: R$0,50 por Km para até 200km e R$0.45 acima de 200km.

distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    preco = distancia * 0.50
    print(f'O preço da passagem é R${preco:.2f}. Boa viagem!')
else:
    preco = distancia * 0.45
    print(f"O preço da passagem é R${preco:.2f}. Boa viagem!")
    
# Fim do exercício 31
