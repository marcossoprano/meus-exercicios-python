
NOME = input("Digite o seu nome:")
N1 = float(input("Digite a nota 1:"))
N2 = float(input("Digite a nota 2:"))
N3 = float(input("Digite a nota 3:")) 


M = (N1 + N2 + N3)/3

if M >= 7:
    R = "está aprovado"
else:
    R = "está reprovado"

print(f"{NOME}, você {R}, com média equivalente a {M}")    


#código refeito usando importando uma biblioteca e usando uma função dela

NOME = input("Digite o seu nome:")
N1 = float(input("Digite a nota 1:"))
N2 = float(input("Digite a nota 2:"))
N3 = float(input("Digite a nota 3:")) 

C = [N1, N2, N3]

from statistics import mean
if mean(C) >= 7:
      R = "está aprovado"
else:
    R = "está reprovado"

print(f"{NOME}, você {R}, com média equivalente a {mean(C)}")    
    