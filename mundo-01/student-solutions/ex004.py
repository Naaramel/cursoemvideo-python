# Exercício 04: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçôes possiveis sobre ele.

valor = input("Digite algo: ")

print("O tipo primitivo desse valor é:", type(valor))
print("Só tem espaços?", valor.isspace())
print("É um número?", valor.isnumeric())
print("É alfabético?", valor.isalpha())
print("É alfanumérico?", valor.isalnum())
print("Está em maiúsculas?", valor.isupper())
print("Está em minúsculas?", valor.islower())
print("Está capitalizada?", valor.istitle())
print("É um dígito?", valor.isdigit())

# Fim do exercício 004
