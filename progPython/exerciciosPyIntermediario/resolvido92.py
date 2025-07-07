conjunto1 = set()
conjunto2 = set()

X = 1
Y = 1

while X != 0:
    X = int(input())
    if X == 0:
        continue
    conjunto1.add(X)
    
print(conjunto1)    


while Y != 0:
    Y = int(input())
    if Y == 0:
        continue
    conjunto2.add(Y)
    
print(conjunto2)    
    
    


conjunto3 = conjunto1.intersection(conjunto2)

print(conjunto3)

conjunto4 = conjunto1.union(conjunto2)

print(conjunto4)