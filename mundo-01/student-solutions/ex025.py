# Exercício 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome completo: ")).strip()

print("Analisando seu nome...")
print(f"Seu nome tem 'SILVA'? {'SILVA' in nome.upper()}")

# Fim do exercício 25