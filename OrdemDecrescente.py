X = float(input("Digite um numero"))
Y = float(input("Digite um numero"))
Z = float(input("Digite um numero"))
if X>Y and X>Z:
    if Y>Z:
        print(X,Y,Z)
    else:
        print(X,Z,Y)
elif Y>X and Y>Z:
    if X>Z:
        print(Y,X,Z)
    else:
        print(Y,Z,X)
elif Z>X and Z>Y:
    if X>Y:
        print(Z,X,Y)
    else:
        print(Z,Y,X)