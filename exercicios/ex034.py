salário = float(input('qual seu salario atual? '))
aumento1 = salário + (salário * 10/100) #calculo de porcentagem
aumento2 = salário + (salário * 15/100)
if salário > 1250:
    print(f'voce recebeu um aumento de 10% e agora vai ganhar {aumento1}')
else:
    print(f'voce recebeu um aumento de 15% e agora vai receber {aumento2}')
