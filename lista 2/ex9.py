P, R = map(int,input().split())



Q = (R/P)*100

if Q >= 0 and Q < 20:
    C = ("4.40% Pessimo")
    
elif Q >= 20 and Q < 40:
    C = ("31.65% Ruim")
    
elif Q >= 40 and Q < 60:
    C = ("56.82% Bom")
    
elif Q >= 60 and Q < 80:
    C = ("80.00% Muito Bom")
    
elif Q >=80 and Q <= 100:
    C = ("94.00% Excelente")


print(f"{Q:.2f}% {C}")    