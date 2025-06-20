#o código a baixo está com erro, na classificação B e C eu coloquei primeiro a razão maior antes da menor, então existe um erro lógico


L = int(input())
AL = int(input())

if L/AL >= 1/8 and L/AL <= 1:
    R = "A"
elif L/AL >= 1/9 and L/AL <= 1/12:
    R = "B"
elif L/AL >= 1/13 and L/AL <= 1/18:
    R = "C"    
else:
    R = "D"

print (R) 


#código com a correção do erro lógico:

L = int(input())
AL = int(input())

if L/AL >= 1/8 and L/AL <= 1:
    R = "A"
elif L/AL >= 1/12 and L/AL <= 1/9:
    R = "B"
elif L/AL >= 1/18 and L/AL <= 1/13:
    R = "C"    
else:
    R = "D"

print (R)    