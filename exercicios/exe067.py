# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

num = int(input('digite um numero inteiro: '))
contagem = 0
multi = 1

while True:
    if contagem == 10:
        num = int(input('digite um numero inteiro: '))
        contagem = 0
        multi = 1
    
    if num == 0:
        break

    contagem += 1
    
    print(f'{num} x {multi} = {num * multi}')
    multi += 1
    
    