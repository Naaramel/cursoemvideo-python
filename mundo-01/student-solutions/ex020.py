# Exercício 20: Um professor quer sortear a ordem de apresentação de um dos seus quatro alunos.  
# Faça um programa que leia o nome dos 4 alunos e mostre sorteada.

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print("A ordem de apresentação será:")
print(alunos)

# Fim do exercício 20
