print(f"Digite as tres distancias : ")
y = float(input( ))
z = float(input( ))
w = float(input( ))

if y > z and y > w:
    print(f'Maior distancia = {y}')

elif z > y and z > w:
    print(f'Maior distancia = {z}')

else :
    print(f'Maior distancia = {w}')