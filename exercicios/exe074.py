# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
menor = 0
maior = 0
numeros = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))

for num in numeros:
    if num == numeros[0]:
        menor = num

    elif num < menor:
        menor = num
    
    elif num > maior:
        maior = num
    
    print(num)

print(f'O maior numero foi {maior}, e o menor foi {menor}')