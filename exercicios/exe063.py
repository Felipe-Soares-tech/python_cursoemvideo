#  Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

num = int(input('digite um numero inteiro: '))
contagem = 1
cont1 = 0
cont2 = 1

while contagem < num:
    contagem += 1
    if contagem == 2:
        print('0 - 1', end='')

    cont = cont1 + cont2
    print(f' - {cont}', end='')

    cont1 = cont2
    cont2 = cont

    

    
    
    
    

    

    

