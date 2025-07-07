#o prgrogrma não estava exibindo o media na mesma linha que o valor final do calculo, tivemos que usar fsring para modificar isso
# e também usamos o END


A = float (input())
B = float (input())
C = [A, B]

from statistics import mean
print ("MEDIA =  ", )
print (mean(C))

#no código abaixo usamos uma função da biblioteca statisticss para calcular uma media de notas, mas só está exibindo 2 casas decimais no máximo


A = float (input())
B = float (input())
C = [A, B]

from statistics import mean
print (f"MEDIA =", end="")
print (mean(C))

#a questão pediu que a média exibida tivesse 5 dígitos, como vamos poder delimitar essa média? temos duas formas 
#usando fstrind:
A = float(input())
B = float(input())
C = [A, B]

from statistics import mean
print(f"MEDIA = {mean(C):.5f}")


#criando uma variável media
A = float(input())
B = float(input())
C = [A, B]

from statistics import mean
media = mean(C)
print(f"MEDIA = {media:.5f}")


#para que a saída tivesse mais precisão importei a biblioteca deciamal

from decimal import Decimal, getcontext
getcontext().prec = 5
from statistics import mean

A = Decimal (input())
B = Decimal (input())
C = [A, B]


print(f"MEDIA  =  {mean(C):.5f}")


