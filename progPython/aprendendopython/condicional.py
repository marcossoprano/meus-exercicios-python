#usando if e else


A = int (input())
B = int (input())



if B == 0:
    print ("divisão não existe")
else  :
    print ((A/B))
    
#usando elif  para limitar as escolhas apenas para números positivos


A = int (input())
B = int (input())



if B == 0:
    print ("divisão não existe")
elif B > 0:
    print ((A/B))