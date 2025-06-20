X = int(input())
Y = int(input())
Z = int(input())

if X == Y and Y == Z:
    R = "equilatero"

elif X != Y and X != Z:
    R = "escaleno"

elif X == Y and X != Z:
    R = "isosceles"

elif X == Z and X != Y:
    R = "isosceles"   

else:

    R= "isosceles"    





