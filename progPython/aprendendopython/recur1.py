






def somaRercusiva (n):
    if n == 1:
        return 1
    else:
        return n + somaRercusiva (n-1)
    
    
n = int(input()) 
print(somaRercusiva(n))   




        
