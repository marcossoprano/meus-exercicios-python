#esse número é primo ou esse número é composto????


X = int(input())

C1 = 1
C2 = 0



while C1 <= X:
  C1= C1 + 1     

  if X % C1 == 0:
     C2 = C2 + 1

     
     
if C2 > 2:
  print("esse número é composto")
  
else:
  print("esse número é primo")       
     
    

     
    
 
       
  

        
        
        
       
        
    
    


