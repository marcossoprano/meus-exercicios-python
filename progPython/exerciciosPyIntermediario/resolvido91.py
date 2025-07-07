from random import randint

I = int(input()) #quantidade de elementos.

if 0 < I <= 50:
    conjunto = set() #criação de um conjunto vazio através da classe set.

    while len(conjunto) < I:  
        conjunto.add(randint(1, 50))

    print(conjunto)
    
    
else:
    print("você digitou um valor fora do intervalo")   



    
    
    
    
    

    
    
