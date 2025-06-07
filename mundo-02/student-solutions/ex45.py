# Desafio 45: Crie um programa que faça o computador jogar Jokenpô (Pedra, Papel ou Tesoura) com você.  

from random import choice
from time import sleep

print('Vamos jogar Jokenpô (Pedra, Papel ou Tesoura)!')
usuario = input('Escolha Pedra, Papel ou Tesoura: ').strip().lower()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)

opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)

print(f'Eu escolhi: {computador}. Você escolheu: {usuario}.')

if usuario not in opcoes:
    print('Opção inválida! Por favor, escolha Pedra, Papel ou Tesoura.')
    exit()
if usuario == computador:
    print(f'Empate! Você também escolheu {usuario}.')
elif (usuario == 'pedra' and computador == 'tesoura') or (usuario == 'papel' and computador == 'pedra') or (usuario == 'tesoura' and computador == 'papel'):
    print(f'Você ganhou! {usuario} vence {computador}.')
else:
    print(f'Você perdeu! {computador} vence {usuario}.')
    
# Fim do desafio 45.
