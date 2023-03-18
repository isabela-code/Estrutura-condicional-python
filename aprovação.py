x = float(input("Digite sua nota : "))
y = float(input("Digite sua segunda nota : "))

soma = x + y

if soma >= 60 : 
    print(f"Parabens, você foi aprovado, sua nota final é de {soma : .1f}")

else: 
    print(f"Se ferrou amigo, sua nota final é de {soma : .1f}")
    print(f"REPROVADO")
