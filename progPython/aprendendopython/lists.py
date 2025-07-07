#Trabalhando com listas: imprimindo a list ou elementos da lista

#Como imprimir a  lista completa???

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (A)


#Como imprimir cada elemento da lista, um a um??? 

i = 0


while  i <= len (A): #a função len contabiliza quantos elementos temos dentro da lista ou string.
   
   print (i)
     
   i += 1 
    
    
#como imprimir apenas um elemento específico da lista

print (A[0])   
    
    
#podemos támbem alterar elementos de uma lista:

A[1] = 200 #aqui eu tó colocando no lugar do elemento de índice igual a 1(2) o valor 200
print (A)    






