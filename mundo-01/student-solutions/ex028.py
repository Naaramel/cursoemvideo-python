# Exercício 28: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# a) Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu. 

from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "pensar" em um número entre 0 e 5

jogador = int(input("Digite um número entre 0 e 5: "))
 
print("Processando...")
sleep(2)

if jogador == computador:
    print("Parabéns! Você venceu!")
else:
    print(f"Você perdeu! O número era o {computador}. Mais sorte na próxima vez!")
    
# Fim do exercício 28