# Exercício 24: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input("Digite o nome da cidade: ")).strip()

print("Analisando a cidade...")
print(f"A cidade começa com 'Santo'? {'SANTO' in cidade[:5].upper()}")

cid = str(input('Em que cidade você nasceu? ')).strip()

print(cid[:5].upper() == 'SANTO')

# Fim do exercício 24