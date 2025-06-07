# Exercício 27: Faça um programa que leia o nome completo de uma pessoa e mostre: 
# a) O primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza | Primeiro nome = Ana | Último nome = Souza

nome = str(input("Digite seu nome completo: ")).strip()

print("Analisando seu nome...")
print(f"Seu primeiro nome é {nome.split()[0]}.")
print(f"Seu último nome é {nome.split()[-1]}.")

# Fim do exercício 27