x = int(input("Digite a quantidade de minutos : "))

if x <= 100:
    pagar = 50

else : 
    minutos = x % 100
    pagar = 50 + (2 * minutos)

print(f"Valor a pagar : R${pagar : .2f}")