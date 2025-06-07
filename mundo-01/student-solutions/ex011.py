# Exercício 11: Faça um programa que leia a largura e a altura de uma parede em metros.
# Depois calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Cada litro de tinta pinta uma área de 2m².

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
tinta_necessaria = area / 2

print(f"A área da parede é {area}m².")
print(f"Você precisará de {tinta_necessaria} litros de tinta para pintá-la.")

# Fim do exercício 11