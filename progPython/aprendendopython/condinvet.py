RISCO = (input("Digite o grau de aceitação de risco (BX para baixo ou AL para alto): "))
VALOR = float (input("Digite o valor a ser investido:"))

if RISCO != ("BX") and RISCO!= ("AL"): 
    INVESTIMENTO = (f"{RISCO} é inválido para o grau de risco")

elif RISCO == ("BX") and VALOR < 1000.00:
     INVESTIMENTO =("poupança")

elif RISCO == ("BX") and VALOR >= 1000.00:
     INVESTIMENTO =("renda fixa")

elif RISCO == ("AL") and VALOR < 1000.00:
     INVESTIMENTO =("BITCOINS")

elif RISCO == ("AL") and VALOR >= 1000.00:
     INVESTIMENTO =("AÇÕES")


print(f"Você deve investir em {INVESTIMENTO}")

#outra forma de fazer esse código 
RISCO = input("Digite BX ou AL para o grau de risco: ") 
VALOR = float(input("Digite o valor: ")) 

if RISCO != ("BX") and RISCO != ("AL"): 
    
    print(f"{RISCO} é inválido para o grau de risco") 
else: 
    if RISCO == ("BX"): 
        if VALOR< 1000.0: 
            r = ("POUPANÇA")
        else: 
            r = ("RENDA FIXA")
    
    else:   
        if VALOR < 1000.0: 
            r = ("BITCOINS") 
        else: 
            r = ("AÇÕES")

print(f"Você deve investir em {r}")
  
