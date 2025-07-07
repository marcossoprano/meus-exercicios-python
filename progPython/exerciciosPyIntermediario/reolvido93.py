from random import randint
I = int(input())

LISTA = []   

for E in range (I): #diferente do exercício anterior, usamos o for justamente com intuito de fazer com que os números gerados possam ser repetidos
    LISTA.append(randint(1,50))

print(LISTA)    
    
    
conjunto5 = set(LISTA)   

print(conjunto5) 


LISTA = conjunto5

print(LISTA)
    
    