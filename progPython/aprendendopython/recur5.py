#função para somar números inteiros de n até 1:
def soma_de_numeros(n):
    if n == 1:
        return 1
    
    else:
        return n + soma_de_numeros(n-1)
    

#função main    
    
n = int(input())    
soma = soma_de_numeros(n)
print(soma)
