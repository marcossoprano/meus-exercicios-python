I = int(input())

if I >= 16:
    if I >= 16 and I < 18 or I > 65:
        R = "eleitor facultativo"
    elif I >= 18:
        R = "eleitor obrigatorio"
else:
    R = "nao eleitor"

print(R)          


# o código acima apresenta algumas redundâncias, eu não precisaria dizer que repetir no primeiro encadeamento o I >=16 e támbem o elif 
#no encadeamento ser trocado por um else.
#código abaixo com as devidas alterações.

I = int(input())

if I >= 16:
    if  I < 18 or I > 65:
        R = "eleitor facultativo"
    else:
        R = "eleitor obrigatorio"
else:
    R = "nao eleitor"

print(R)              


