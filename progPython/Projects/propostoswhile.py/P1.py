S = 0
Q = 0


X = 1

while X != 0:
    X = int(input())
    
    S = S + X
    
    Q = Q + 1
    
    X = int(input())
    
    
print(f"{S}\n{Q}")


#esse exercício pedia para nós fazermos a soma de números que fosem adicionados em loop e ao ser parado o loop, quando o ususário digitasse
#10 essa soma deveria serr impressa junto com a quantidade de números que foram digitados.
#Mas, o programa acima apresentava uma incosist~encia, em virtude que o 0 era totalizado junto e quantizado, sendo que ele
# só deveria servir para encerrar o lopp. A solução implemntada poderia ser colocar um if para que soma e a contegem só fosse feita quando
# o usuário digitasse um número que fosse diferente de zero, reforçando a nossa primissa do while, mas o exercício pedia outra alternativa
# e que essa no envolvesse o uso de  condicionais if e else
# a solução consistia em fazer com que a incialização da variável X não ser 1 como estava incialmente e também trocar a posição do input, para 
#para que ele só recebesse o valor depois, s

#a primeira entrada deveria ser feita fora do loop e ter outra entrada em baixo da soma e da quantização, isso garantiria que ao digitar zero
#o programa já se encerra se e não contabilizaria o zero, além disso, se já estivesse dentro do loop, ao adicionar 0 ele não conseguoria voltar 
#lá em cima e descer para ser printado, porque obviamente ele seria zero.






S = 0
Q = 0


X = int(input())

while X != 0:
    
    
    
    S = S + X
    
    Q = Q + 1
    
    X = int(input())
    
    
print(f"{S}\n{Q}")
    
    
