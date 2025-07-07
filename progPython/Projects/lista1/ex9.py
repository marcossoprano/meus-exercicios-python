#Calculo do salário de um funionário, usei ao invés de dois prints a formulação em fstring e os placeholdrs

N = int(input())
H = int(input())
Valor_hora = float(input())

S = (H*Valor_hora)

print (f" NUMBER = {N}\nSALARY = R$ {S:.2f}")
