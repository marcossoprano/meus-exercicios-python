def contagemRegressiva(n):
    if n == 1:
        print (n)
        
    
    else:
        print(n)
        contagemRegressiva(n-1)
        
        
    
    
n = int(input())  

contagemRegressiva(n)