try:

  texto = "Linha de calçados:"

  LL = int (input())

  match LL:
      case 16: 
        print(f"{texto} bebê")
      case 23:    
        print(f"{texto} infatil feminino")
      case 25:
        print(f"{texto} infaltil esportivo")   
      case 29:
        print(f"{texto} Masculino formal")
      case 42:
        print(f"{texto} Msculino europeu ")
      case 43:
        print(f"{texto} Masculino casual")   
                   
        
        
except ValueError:  
        print("Código digitado é invalido")