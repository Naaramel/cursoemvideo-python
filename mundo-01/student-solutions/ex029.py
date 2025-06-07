# Exercício 29: Escreva um programa que leia a velocidade de um carro
# a) Se ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# Valor da multa: R$7,00 por cada Km acima do limite.

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    print(f"Você foi multado! A multa é de R$ {(velocidade - 80) * 7:.2f}.")
elif velocidade == 80:
    print("Você está na velocidade limite. Mantenha a atenção!")
else:
    print("Você está dentro do limite de velocidade. Continue dirigindo com segurança!")
    
# Fim do exercício 29 