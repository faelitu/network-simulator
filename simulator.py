import random as rd
import math

rd.seed()

def aleatorio():
    u = rd.random() # Generate a number between [0.0, 1.0)
    u = 1.0 - u # Returns a number between (0.0, 1.0]
    return u

# MAIN:
l = float(input("Informe o valor medio: ")) # l == exponencial parameter.
l = 1.0 / l                                 # E[X] == 1/l

soma = 0.0
qtd = 10000
for cont in range(0, qtd):
    valor = float((-1.0/l) * math.log(aleatorio()))
    print("Valor gerado: " + str(valor))
    soma += valor
print("Media: " + str(soma/qtd))