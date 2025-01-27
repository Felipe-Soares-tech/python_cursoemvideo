#  Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120

multi = 1
num = int(input('digite um numero: '))
for i in range (num, 0, -1):
    if i > 1:
        print(i, 'x ' ,end= '')
    else:
        print(i, '= ', end='')
    multi *= i

print(multi)






