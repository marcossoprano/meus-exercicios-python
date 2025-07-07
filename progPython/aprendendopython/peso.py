NOME = str(input("Qual o seu nome?"))
PESO = float(input("Qual o seu peso?"))


if PESO < 52:
    CATEGORIA = (f" o peso {PESO} tem categoria inválida")
    
else:
    if PESO >= 52 and PESO < 65:
        CATEGORIA = (f" o peso {PESO} te coloca na categoria pena")
    elif PESO >= 65 and PESO < 72:
        CATEGORIA = (f"o peso {PESO} te coloca na categoria leve")
    elif PESO >= 72 and PESO < 79:
        CATEGORIA = (f"o peso {PESO} te coloca na categoria ligeiro")
    elif PESO >= 79 and PESO < 86:
        CATEGORIA = (f"o peso {PESO} te coloca na categoria meio-médio")
    elif PESO >= 86 and PESO < 90:    
        CATEGORIA = (f"o peso {PESO} te coloca na categoria médio")
    elif PESO >= 90 and PESO < 100: 
        CATEGORIA = (f"o peso {PESO} te coloca na categoria meio-pesado")
    else:
        CATEGORIA = (f"o peso {PESO} te coloca na categoria pesado")
print (CATEGORIA)


#outra forma de contruir esse código:


NOME = str(input("Qual o seu nome?"))
PESO = float(input("Qual o seu peso?"))


if PESO < 52:
    CATEGORIA = (f" o peso {PESO} tem categoria inválida")
    
else:
    if PESO >= 52 and PESO < 65:
        CATEGORIA = (f" o peso {PESO} te coloca na categoria pena")
    elif PESO >= 65 and PESO < 72:
        CATEGORIA = (f"o peso {PESO} te coloca na categoria leve")
    elif PESO >= 72 and PESO < 79:
        CATEGORIA = (f"o peso {PESO} te coloca na categoria ligeiro")
    elif PESO >= 79 and PESO < 86:
        CATEGORIA = (f"o peso {PESO} te coloca na categoria meio-médio")
    elif PESO >= 86 and PESO < 90:    
        CATEGORIA = (f"o peso {PESO} te coloca na categoria médio")
    elif PESO >= 90 and PESO < 100: 
        CATEGORIA = (f"o peso {PESO} te coloca na categoria meio-pesado")
    else:
        CATEGORIA = (f"o peso {PESO} te coloca na categoria pesado")

print (CATEGORIA)

