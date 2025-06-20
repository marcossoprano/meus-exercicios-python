#situação de um aluno


A = int(input())
B = int(input())
C = int(input())

L = [A, B, C]

from statistics import mean

if mean(L) >= 70 and mean(L) <= 100:
  situacao = "APROVADO"

elif mean(L) >= 0 and mean(L) < 40:
    situacao = "REPROVADO"

elif mean(L) >= 40 and mean(L) < 70:
        
     situacao = "FINAL"
else: 
     print("Media invalida")     
     

print(f"A media do aluno foi {mean(L):.2f} e ele foi {situacao}")     
       


