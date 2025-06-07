# Exercício 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# As três retas podem formar um triângulo se a soma de quaisquer duas delas for maior que a terceira.   

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
    
# Fim do exercício 35

# Extra: Verificar se o triângulo é equilátero, isósceles ou escaleno.

if r1 == r2 == r3:
    print("O triângulo é EQUILÁTERO.")
elif r1 == r2 or r1 == r3 or r2 == r3:
    print("O triângulo é ISÓSCELES.")
else:
    print("O triângulo é ESCALENO.")