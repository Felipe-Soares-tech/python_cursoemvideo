# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e 
# o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

saque = int(input('gostaria de sacar quando? '))
notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0
while True:
    if saque - 50 >= 0:
        notas50 += 1
        saque -= 50
    
    elif saque - 20 >= 0:
        notas20 += 1
        saque -= 20

    elif saque - 10 >= 0:
        notas10 += 1
        saque -= 10

    elif saque - 1 >= 0:
        notas1 += 1
        saque -= 1

    elif saque == 0:
        break

print(f'''notas50: {notas50}
notas20: {notas20}
notas10: {notas10}
notas1: {notas1}''')
    
