# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.


num = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
cont1 = num
cont = 0

while cont < 10:
    cont += 1

    if cont1 == num:
        print(num, '-> ', end= '')

    cont1 += num2
    if cont < 10:
        print(cont1, '-> ', end= '')
    elif cont == 10:
        print(cont1, end='')


# num = int(input('Digite o primeiro termo: '))
# num2 = int(input('Digite a razão da P.A.: '))
# cont1 = num
# cont = 0
# total = 0
# mais_termos = 10

# while mais_termos != 0:
#     total += mais_termos
#     while cont < total:
#         cont += 1

#         if cont1 == num:
#             print(num, '-> ', end='')

#         cont1 += num2
#         if cont < total:
#             print(cont1, '-> ', end='')
#         elif cont == total:
#             print(cont1, end='')

#     print()  # Para nova linha após exibir os termos
#     mais_termos = int(input('Quantos termos você quer mostrar a mais? '))

# print('Progressão encerrada com {} termos mostrados.'.format(total))