X = int (input())
Y = int (input())

if X == Y:
 R = (f"{X} é igua a {Y}")
  
elif X > Y:
 R= (f"{Y} é menor")

else:
 R = (f"{X} é menor")

print (R)

# o primeiro if foi desnecessário porque se um dos dois números já não for menor, já concluimos que deverá ser execultadono else, 
# sendo assim podendo ser exibidos qualquer um dos valores que que esteja disscriminado na linha do else!

#OUTRA FORMA DE ESCREVER O CÓDIGO CASO FOSSE DITO NO ENUNCIADO QUE TERIAMOS QUE DIZER QUE OS DOIS NÚMEROS SÃO IGUAIS.


X = int (input())
Y = int (input())

if X == Y:
  R = (f"{X} é igua a {Y}")

else:
   
  if X > Y:
     R= (f"{Y} é menor")

  else:
     R = (f"{X} é menor") 
     
  print (R)   


