x = input("Voce vai digitar a temperatura em qual escala (C/F)? : ")

if x == 'C':
    y = float(input("Digite a temperatura em Celsius : "))
    T = (y * 1.8) + 32
    print(f'Sua temperatura em Fahrenheit é : {T : .2f}')
else :
    y = float(input("Digite a temperatura em Fahrenheit : "))
    T = (y - 32)*(5/9)
    print(f'Sua temperatura em Celsius é : {T : .2f}')
