level = int(input())


if level >= 1 and level <= 20:
  P = 20 + (level**3)
elif level > 20 and level <= 40:
  P = 	8000 + (level - 10**2)
elif level > 40 and level <= 60:
  P =  9000 + (5*level )
elif level > 60 and level <= 80:
  P = 9300 + (2*level)
else:
  P = 9500 + level  

print (f"Potencia de : {P} W")  



#thehusley está mostrando erro de apresentação.