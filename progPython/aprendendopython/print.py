x = 2500
y = 6999
s = x + y

print ( "a soma de", x, "com", y, "é:", s)


#como deixar esse código mais organizado, mais especificamente, como organizar a linha 5. 
#podemos usar o comando format junto na linha do print


print ("a soma dos valores {0} e {1} é {2}" .format (x, y, s))


#conseguimos deixar o código ainda mais elegante e organizado com o uso de fstring

print(f"a soma de {x} com {y} é {s}")

#como podemos notar no código acima, continuamos exibindo amema mensagem só que agora já colocamos os paramentros direto na linha de código
#isso torna a leitura do código mais polida e de fácil compreensão.


