num = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
cont1 = num
cont = 0
total = 0
mais_termos = 10

while mais_termos != 0:
    total += mais_termos
    while cont < total:
        cont += 1

        if cont1 == num:
            print(num, '-> ', end= '')

        cont1 += num2
        if cont < total:
            print(cont1, '-> ', end= '')
        elif cont == total:
            print(cont1, end='')

        print()  # Para nova linha após exibir os termos
        mais_termos = int(input('Quantos termos você quer mostrar a mais? '))


#




