D = int(input())
X = 1
if D > 0:

 while X < 100:
    if X % D == 0:
     print (X)
    X = X + 1  
    
else:
    print("só é aceitos números positivos diferentes de 0")
        