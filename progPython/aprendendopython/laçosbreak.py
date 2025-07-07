

X = 1

while True:
     X = int(input())
     if X == 0:
          break 
     print(X)
     
#o comando break vai parar definitivamente a execução do programa, enquanto o comando continue anula apenas ama das interações com a condição.
# no programa acima a gente tem que enquanto a entrada for veradeira, ou seja, enquanto adicionarmos um número inteiro 
# o programa irá printar esse número para o usuário, mas ao adicionarmos uma condição verificamos que sse programa será paralisado
# quando o usuário digitr o número 0.
# poderiamos reescrever esse programa da seguinte maneira:

X = 1


while X != 0:
     X = int(input())
    
     print (X)     


#qual o problema do código a baixo?
X = 1
X = int(input())

while X != 0:
    
    
     print (X)     


     