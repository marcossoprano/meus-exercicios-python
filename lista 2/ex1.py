#merceária do ambrósio, depois tentar fazer usando dicionário, lista, criando funções

P = int(input("digite o código do produto:"))
Q = int(input("digite a quantidade comprada"))



if P == 1:
    V = (Q * 5.30)

elif P == 2:
    V = (Q*6.0)

elif P == 3:
    V = (Q*3.20)

else: 
    V = (Q * 2.50)


if (V >= 40) or (Q >= 15):
    print (f"R$ {V * 0.85:.2f}")

else: 
    print(f"R$ {V:.2f}")     



