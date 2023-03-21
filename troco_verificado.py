x = int(input("Preço unitario do produto : "))
y = int(input("Quantidade comprada : "))
z = int(input("Dinheiro recebido : "))

troco = z - (x*y)
preço = x*y 
restante = (x*y) - z

if z < preço:
    print(f"Dinheiro insuficiente. Faltam {restante :.2f} reais")

else : 
    print(f"Troco = {troco :.2f} reais")