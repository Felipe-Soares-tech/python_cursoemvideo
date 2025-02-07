# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

num = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
cont1 = num
cont = 0
mais_termos = 10

while cont < mais_termos:
    cont += 1

    if cont1 == num:
        print(num, '-> ', end= '')

    cont1 += num2
    if cont < mais_termos:
        print(cont1, '-> ', end= '')

    elif cont == mais_termos:
        cont = 0
        print(cont1)
        mais_termos = int(input('deseja mostrar mais termos? se sim, quantos? '))
    
    elif mais_termos == 0:
        break
    
    
    
    


#




