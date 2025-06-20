TIPO = input("digite o tipo, D, E ou L:")
VALOR = float(input("digite quanto dessa moeda você quer comprar, a conversão será realizada:"))



if TIPO == "D":
   R = VALOR * 4.89 
elif TIPO == "E":
   R = VALOR * 5.26
else:    
   R = VALOR * 6.17 

print(f"{R:.2f}R$")   

