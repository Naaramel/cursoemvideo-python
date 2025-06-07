# Desafio 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa deve perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário. Caso ultrapasse esse limite, o empréstimo será negado. 

from time import sleep 

print('Bem-vindo ao programa "Minha Casa, Minha Dívida".')

casa = float(input("Digite o valor da casa desejada: R$"))
salario = float(input("Agora digite o valor do seu salário: R$"))
tempo = int(input("Agora digite em quantos anos você deseja pagar: "))

prestacao = casa / (tempo * 12)
limite = salario * 0.3

print("Analisando os seus dados. Aguarde...")
sleep(3)

if limite > prestacao:
    print('Parabéns, o seu empréstimo foi aprovado. Você já pode comprar a sua casa!')
else:
    print(f'Que pena, o seu empréstimo não foi aprovado...\nHora de pedir um aumento para o seu chefe ;).\nO seu atual limite é de R${limite}.\nO valor da sua parcela para pagamento em {tempo} anos é de R${prestacao}.\nVocê precisa de R${prestacao - limite} a mais por mês para conseguir comprar a sua casa nova ')

# Fim do desafio 36