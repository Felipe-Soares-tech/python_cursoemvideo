# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas 
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

num = 1
numeros = []
pares = []
impares = []

while num > 0:
    num = int(input('digite um numero: '))
    numeros.append(num)
    pares.append(num) if num%2 == 0 else impares.append(num)

print(f'todos os numeros: {numeros}')
print(f'numeros pares: {pares}')
print(f'numeros impares: {impares}')