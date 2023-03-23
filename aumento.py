x = float(input('Digite o salario da pessoa : '))

if x <= 1000:
    novo = (x * 0.20) + x
    aumento = x * 0.20
    print(f'Novo salario = R${novo : .2f}')
    print(f'Aumento = R${aumento : .2f}')
    print(f'Porcentagem = 20 %')
elif x > 1000 and x <= 3000:
    novo = (x * 0.15) + x
    aumento = x * 0.15
    print(f'Novo salario = R${novo : .2f}')
    print(f'Aumento = R${aumento : .2f}')
    print(f'Porcentagem = 15 %')
elif x > 3000 and x <= 8000:
    novo = (x * 0.10) + x
    aumento = x * 0.10
    print(f'Novo salario = R${novo : .2f}')
    print(f'Aumento = R${aumento : .2f}')
    print(f'Porcentagem = 10 %')
else : 
    novo = (x * 0.05) + x
    aumento = x * 0.05
    print(f'Novo salario = R${novo : .2f}')
    print(f'Aumento = R${aumento : .2f}')
    print(f'Porcentagem = 5 %')
    