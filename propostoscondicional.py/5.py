I = int(input("digite a sua idade:"))

if I > 16:
    if I < 18 and I >= 65:
        print("eleitor facultativo")
    elif I >= 18 and I < 65:
        print("eleitor obrigatório")   
else:
    print("não eleitor")         