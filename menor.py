x = float(input("Digite o primeiro numero : "))
y = float(input("Digite o segundo numero : "))
z = float(input("Digite o terceiro numero : "))

if x < y:
    if x < z :
        print(f"Menor numero é = {x}")

elif y < x :
    if y < z :
        print(f"Menor numero é = {y}")
        
else : 
    print(f"Menor numero é = {z}")

