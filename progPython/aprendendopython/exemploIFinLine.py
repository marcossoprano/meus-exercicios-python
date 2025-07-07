Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216]

#filtre os números entre 150 e 200 e os coloque em uma lista 


L = [] #criação de uma lista vazia

for elemento in Codigos:
   L.append(elemento) if elemento >= 150 and elemento <= 200 else 0 #o zero no else faz com que ele não retone nada
   
   
   
   
print(L)   
   