# Desafio 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# 1) Média abaixo de 5.0: REPROVADO
# 2) Média entre 5.0 e 6.9: RECUPERAÇÃO
# 3) Média 7.0 ou superior: APROVADO 

print('Bem-vindo ao portal do aluno.\nDigite as notas das suas provas e veja se foi aprovado.')

prova1 = float(input('Nota prova 01: '))
prova2 = float(input('Nota prova 02: '))
prova3 = float(input('Nota prova 03: '))

aprovado = 7
recuperacao = 5

media = (prova1 + prova2 + prova3) / 3

if media >= aprovado:
    print('Parabéns, você foi APROVADO!')
elif media < aprovado and media >= recuperacao:
    print('Você está de RECUPERAÇÃO.\nAinda dá tempo de recuperar, estude para a prova!.')
elif media < recuperacao:
    print('Você foi REPROVADO.\nVocê pode tentar novamente no próximo semestre.')
else:
    print('Ocorreu um erro. Tente novamente mais tarde.')
    
# Fim do desafio 40 