#cálculo dos termos da pa

P = int(input()) #primeiro termo
R = int(input()) #razão
Q = int(input()) #quantidade de termos

C = 1

LISTA = [P]

while C < Q:
    
    
    P = P + R
    
    LISTA.append(P)
   
    C = C + 1
   
print(LISTA)  



########



