#exercício proposto 78: ler uma data string e depois separar ela em dia, mês e ano;

X = input() #recebe a data

Q = len(X) #ussamos a função len para quantificar quantos números tem a string recebida




D1 = int (X[0:2]) #fatiamento para o dia
D2 = int (X[2:4]) #fatiamento para o mês 
D3 = int (X[4:] ) #fatiamento para o ano


#armazenamos esses fatiamentos em variáveis distintas para depois formatá-los em uma variável R que dirá a data caso a tring digitada seja válida
#ou dirá que não é válida caso a string digita tenha menos que 8 digito ou letras no meio

if X.isnumeric() and Q == 8:
    if (D3 % 4 == 0 and  D3 % 100 != 0) or (D3 % 400 == 0):
        fevereiro = 29
        
    else:
        fevereiro = 28
        
        
MESES = [31, fevereiro, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #criei uma lista para definir qual é o valor máximo que cada mês pode assumir
        

if D1 >= 1 and D1 <= MESES[D2 - 1]:
     R = (f"a data é {D1}/{D2}/{D3}") 
    
    
else:
    R = ("essa data não é válida")
    
    
    
print (R)        
       
        
        
        
        
            
    

