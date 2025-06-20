X = int(input("digite um número que esteja dentro do intervalo fechado de 100 a 200:"))

while X < 100 or X > 200:
    
    X = int(input("digite um número que esteja dentro do intervalo fechado de 100 a 200:"))
    if X < 100 or X > 200:
     
     print(f"{X} esse valór não está no intervalo, por favor digite um valor válido:")
     
     
     
else:
   print ("esse valor é valido")    
      
      
#a primeira olhada podemos até achar que esse programa está corret, mas, qual o erro?
#basicamente, ao rodar o programa pela primeira vez, todas as mensagens, independete do número serão printadas de forma correta, 
#uma vez que o número entrará logo no input em cima do while, e não passará pela prime vez no loop.
#ao entrar em loop o programa apresentará um erro para os números que estiverem dentro no intervalo, isso porque independente do valor que for
#digitado o programa irá ler e printar a primeira mensagem, mesmo que ele esteja no intervalo correto exigido.
#para resolver isso, basta que nós adicionemos uma condição id dentro do while para que dentro do while só seja printada a mensagem 
#de erro apenas quando o número estiver fora da condição while descrita logo acima.      