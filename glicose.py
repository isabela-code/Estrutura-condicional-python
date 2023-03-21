x = float(input("Digite a medida da glicose : "))

if x <= 100:
    print(f"Classificação : normal")
elif x > 100 and x <= 140 :
    print(f"Classificação : Elevado")
else :
    print(f"Classificação : Diabetes")