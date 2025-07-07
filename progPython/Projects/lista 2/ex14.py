M = int(input())

P = 0 


if M <= 10: 
    P = 7 

elif M <= 30: 
    P = (M - 10) * 1 + 7  # o valor 1 tem que multiplicar apenas a parte que excede de do parametro 10

elif M <= 100: 
    P = (M - 30) * 2 + (30 - 10) * 1 + 7 # o valor 2 tem que multiplicar apenas a parte que execede de 30

elif M <= 1000:
   P = (M - 100) * 5 + (100 - 30) * 2 + (30 - 10) * 1 + 7 # o multiplicador 5 tem que multiplicar a parte que execede de 100 



print(f"{P}")
