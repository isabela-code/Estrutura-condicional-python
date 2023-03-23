x = int(input('Digite o codigo do produro comprado : '))
y = int(input('Digite a quantidade comprada : '))

if x == 1:
    produto = 5 * y 
    print(f"Total a pagar : {produto : .2f}")
elif x == 2:
    produto = 3.5 * y 
    print(f"Total a pagar : {produto : .2f}")
elif x == 3:
    produto = 4.8 * y 
    print(f"Total a pagar : {produto : .2f}")
elif x == 4:
    produto = 8.9 * y 
    print(f"Total a pagar : {produto : .2f}")
else :
    produto = 7.32 * y 
    print(f"Total a pagar : {produto : .2f}")