# Exercício 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$ 5,63 (Cotação de 04/06/2025).

real = float(input("Digite quanto dinheiro você tem na carteira: R$ "))
dolar = real / 5.63 

print(f"Com R$ {real}, você pode comprar US$ {dolar:.2f}.")

# Fim do exercício 10
