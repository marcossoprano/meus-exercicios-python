A = float(input())
B = float(input())
C = float(input())

if A == B and A == C:
    R = 1

elif A == B and A != C:
    R = 3

elif B == C and B and A != C:
    R = 3

elif A == C and B != C:
    R = 3

else:
    R = 2

print(R)    


