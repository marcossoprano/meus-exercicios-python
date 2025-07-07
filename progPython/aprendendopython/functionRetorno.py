#def lerInteiro():
 #   n = int(input())
  #  return n

#n = lerInteiro()
#print(f"-----{n}--------------") 

from random import randint 

def carregamentoLista(quantidade):
    
    Lista = []
    for elemento in range (quantidade):
        Lista.append(randint(1,1000))
        
    return Lista

#main/////////////////////////////////////////////

quantidade = int(input())
Lista = carregamentoLista(quantidade)
print(Lista)



    
    
    
    
        
    


