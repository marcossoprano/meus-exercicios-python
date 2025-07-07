S = float(input("digite o seu salário:"))
P = float(input("digite o calor da parcela:"))

p= S*0.08

if P < p:
    print("empréstimo concedido.")
else:
    print("empréstimo não pode ser concedido, você pode tentar de novo depois.")    
