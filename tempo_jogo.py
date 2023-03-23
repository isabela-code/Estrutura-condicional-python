x = int(input('Hora inicial : '))
y = int(input('Hora final : '))

if x < y:
    final = y - x
else : 
    final = (24 - x)+y

print(f'O jogo durou {final} hora(s)')