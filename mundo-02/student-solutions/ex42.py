# Desafio 42: Refaça o desafio 35 dos triângulos, acrescentando o recurso de identificar o tipo de triângulo formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
    
if r1 == r2 == r3:
    print("O triângulo é EQUILÁTERO.")
elif r1 == r2 or r1 == r3 or r2 == r3:
    print("O triângulo é ISÓSCELES.")
else:
    print("O triângulo é ESCALENO.")
    
# Fim do exercício 42
