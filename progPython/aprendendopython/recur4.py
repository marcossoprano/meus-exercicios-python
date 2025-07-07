def potencia(x, n):
    if n == 0:
       return 1
        
    else:
       return  x * potencia(x, n - 1)
       
       
       
x = int(input())       
n= int(input())       

print(potencia(x, n))