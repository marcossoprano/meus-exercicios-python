P = float(input())
V = float(input())

if V <= P:
    M = 0.00
    C = 0

elif V <= 1.2*P: 
    M =  85.13
    C = 4

elif V <= 1.5*P:
    M = 127.69
    C = 5
    

else:
    M =  574.62
    C = 7
    
print (f"{M}\n{C}")    