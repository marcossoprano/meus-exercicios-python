#menor de 3

X = int(input()) 
Y = int(input())
Z = int(input())

if X < Y and X < Z:
    print(X)


elif Y < X and Y <= Z:
    print(Y)  


elif Z < X and Z < Y:
    print(Z) 



else:
    print (X) 


