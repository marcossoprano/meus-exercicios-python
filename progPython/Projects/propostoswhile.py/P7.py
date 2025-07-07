Q = int(input())
S = 0

while Q > 0:
    S = S + Q
    Q = int(input())
    
else:
    print("você digitou um número que não é permitido")    
    
print (S)    

##########################################################################################################################
    
    
#outra maneira de fazer esse programa:



# Inicializa a variável para armazenar a soma total
soma = 0

while True:
    # Lê a entrada do usuário
    quantidade = int(input("Digite a quantidade de produtos vendidos (0 ou negativo para sair): "))
    
    # Verifica se a entrada é zero ou negativa para encerrar o laço
    if quantidade <= 0:
        break
    
    # Adiciona a quantidade ao total
    soma += quantidade

# Exibe o total de quantidades
print(f"A soma de todas as quantidades digitadas é: {soma}")
    