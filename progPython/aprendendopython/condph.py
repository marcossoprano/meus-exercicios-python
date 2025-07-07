#refazer essa questão


PH = float(input())

if PH < 6:
    print("solução é ácida")
elif PH >= 6 and PH < 7:
    print("Solução levemente ácida ")
elif PH == 7: 
    print("Solução neutra ")    
elif PH > 7 and PH <= 8:
    print("solução levemente alcalina")
else: 
    print("solução alcalina") 

#outra forma de fazer que gastaria menos memória e a arquiterura do código ficaria mais eficiente
#criariamos uma variável que iria trocar de valor durante o código de acordo com a faixa de ph


PH = float(input())

if PH < 6:
    r = ("solução é ácida")
elif PH >= 6 and PH < 7:
    r = ("Solução levemente ácida ")
elif PH == 7: 
    r = ("Solução neutra ")    
elif PH > 7 and PH <= 8:
    r = ("solução levemente alcalina")
else: 
    r = ("solução alcalina") 
    print (r)
