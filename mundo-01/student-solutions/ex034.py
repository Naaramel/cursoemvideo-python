# Exercício 34: Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento:
# 1) Salários maiores R$1250.00, o aumento será de 10%.
# 2) Salários menores ou iguais a R$1250.00, o aumento será de 15%.

salario = float(input("Digite o salário do funcionário: "))

if salario > 1250.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f"O aumento será de R$ {aumento:.2f}.")