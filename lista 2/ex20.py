L = float(input())
T = str (input())

if T == ("G"):
    if L <= 20:
     P = L * 2.50*0.96
    else:
     P =  L * 2.50*0.94

elif T == ("A"):  
    if L <= 20:
     P = L * 1.90*0.97
    else:
     P = L * 1.90*0.95

elif T == ("D"):
    if L <= 25:
     P = L*1.66
    else:
     P = L*1.66*0.96

print(f"R$ {P:.2f}")    


