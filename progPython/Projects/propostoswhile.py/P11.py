#sequência de fibonacci

N = int(input())
C = 0 #contador


a1 = 0
a2 = 1



while C < N:
    print (a1)
    a1, a2 = a2, (a1+a2)   #a1, vira a2 e a2 vira (a1+a2)q
    
    C = C+1 
    
