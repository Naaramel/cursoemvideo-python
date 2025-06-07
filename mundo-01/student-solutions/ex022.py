#  Exercício 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas e minúsculas.
# 2) Quantas letras ao todo (Sem considerar espaços).
# 3) Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "))

print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.")

primeiro_nome = nome.split()[0]

print(f"Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.")
# Fim do exercício 22

