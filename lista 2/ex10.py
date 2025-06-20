#no código a baixo faltou o caso de B == C

A, B, C = map(int, input().split())

if A + B == C:
    print("S")
        
elif A + C == B:  
    print("S")

elif B + C == A:
     print("S")

elif A == B:
     print("S")

elif A==C:
     print("S")   

else:
     print("N")       


#CÓDIGO CORRIGIDO

A, B, C = map(int, input().split())

if A + B == C:
    print("S")
        
elif A + C == B:  
    print("S")

elif B + C == A:
     print("S")

elif A == B:
     print("S")

elif A == C:
     print("S")   
     
elif B == C:
     print("S")   
     
     
     

else:
     print("N")       



