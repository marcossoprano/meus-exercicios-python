#tratamento de exceções em python



A = int(input())
B = int(input())

try: #comporta o código que deve ser executado corretamente
    
    X = A/B
    print (X)

except: #trata possíveis erros no código
    print("não é possível realizar a divisão")
    
    #nessa situação o try faz com que o código não pare de funcionar mesmmo que o usuário digite uma divisão por 0, a baixo ficaria o código
    #se ao invés de usarmos o try e o except, usassemos o if e else tradicionalmente.
    
    
A = int(input())
B = int(input())



if B == 0:
    print("não é possível fazer a divisão")
    
else:
    X = A/B 
    print(X) 
          
    
    