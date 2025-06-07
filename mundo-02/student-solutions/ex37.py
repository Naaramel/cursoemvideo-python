# Desafio 37: Escreva um programa que leia um número inteiro qualquer e permita ao usuário escolher a base de conversão:
# 1) para binário
# 2) para octal
# 3) para hexadecimal

print("Bem-vindo ao conversor de bases numéricas!")

numero = int(input("Digite um número inteiro: "))

opcao = int(input("Escolha a base de conversão:\n1) Binário\n2) Octal\n3) Hexadecimal\nDigite a opção desejada (1/2/3): "))

if opcao == 1:
    print(f"{numero} em binário é {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} em octal é {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} em hexadecimal é {hex(numero)[2:]}")
else:
    print("Opção inválida!")   
    
# Fim do Desafio 37    