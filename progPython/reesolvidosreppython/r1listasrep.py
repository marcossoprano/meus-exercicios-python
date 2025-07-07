A1 = int(input())
R = int(input())
Q = int(input())

L = [A1]

i = 1


while i < Q:
    A1 = A1 + R #não precisa multiplicara razão pelo contador pelo fato de que já estamos acumulando valores detro da variável A
    L.append(A1)
    i = i + 1
    
    
    
print (L)    
    

#usando o for:

    
A1 = int(input())
R = int(input())
Q = int(input())
i = 1

L = [A1]

for i in range(i, Q):
    A1 = A1 + R
    L.append(A1)

print(L)