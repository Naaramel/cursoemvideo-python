# Exercício 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e calcule o comprimento da hipotenusa.

import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}.")

# Fim do exercício 17