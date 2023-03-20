x = float(input("Digite o primeiro coeficiente : "))
y = float(input("Digite o segundo coeficiente : "))
z = float(input("Digite o terceiro coeficiente : "))

b = (y**2) -4*x*z

if b == 0 :
    x1 = ((-y) + (b ** 1/2))/(2*x)
    x2 == x1

elif b > 0 :
    x1 = ((-y) + (b ** (1/2)))/(2*x)
    x2 = ((-y) - (b ** (1/2)))/(2*x)
    
else :
    print(f"Equação não possui raizes reais")
    
print(f"X1 = {x1 : .4f}")
print(f"X2 = {x2 : .4f}")
    