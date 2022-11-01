a = float(input ("Lado a = "))
b = float(input ("Lado b = "))
c = float(input ("lado c = "))

if (a < b + c and b < a + c and c < b + c):
    if (a == b and b == c):
        print("\nOs lados formam um triangulo equilatero e sua área é de", a*b*c )
    else:
        print("\nOs lados não formam um triangulo")

sair = input("\nDigite ENTER para sair...")