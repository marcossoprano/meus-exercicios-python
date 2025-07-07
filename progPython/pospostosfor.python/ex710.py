X = int(input())

Q = []

i = 0

for i in range (i, X):
    N = int(input())
    Q.append(N)
    
print (Q)    

Q2 = []

i2 = 0
Y = 1

while Y > 0:
    
    Y = int(input())

    i2 += 1
    if Y == 0:
        break
    Q2.append(Y)
    
Q2.append(Y)
  
     
i3=0  

for Y in Q2:  
    
    while Y in Q:
     Q.remove(Y)
    i3 += 1
    
print(Q)    
    
  
    
    
    