# Exercício 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa leia o nome e escreva o nome do escolhido.

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

escolhido = random.choice([aluno1, aluno2, aluno3, aluno4])

print(f"O aluno escolhido foi {escolhido}.")        

# Fim do exercício 19