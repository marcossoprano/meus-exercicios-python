#programa pra ler números e colocar em um artigo até que o usuário digite 0:

arquivo = open ('gravação.txt', 'w')#abertura do arquivo

foiescrito = int(input())

while foiescrito != 0:
    
    arquivo.write(f"{foiescrito} " + "\n")
    foiescrito = int(input())
arquivo.close() #fechamento do arquivo


#agora vamos ler o arquivo criado 

arquivo = open ('gravação.txt', 'r') #abertura do arquivo

leituradeaquivo = arquivo.read()

print(leituradeaquivo)


#usando o método writeline(deixa tudo na mesma linha)
#prencha uma lista e a escreva em uma lista, o usuário deve digitar os elementos da lista até que ele digite 0 e a execução pule do loop 




arquivo2 = open("gravação.txt", "w") #abertura do arquivo

lista = []
x = int(input())

while x != 0:
    arquivo.write(f"{foiescrito}")
    lista.append(x)
    x = int(input())


arquivo2.close()