#esse número é primo ou composto usando o for
 
N = int(input())   

i = 1
i2= 0


for i in range (i, N+1):
  
  if N % i == 0:
      i2 +=1
      
      
if i2 > 2:
    print("esse número é composto")      
    
else: 
    print("esse número é primo")    
      
      
    
      
     