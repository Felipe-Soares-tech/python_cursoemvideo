# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:


# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

# for i in range(4):
#     num = int(input('digite um numero: '))




num1 = int(input('digite um numero: '))
num2 = int(input('digite um numero: '))
num3 = int(input('digite um numero: '))
num4 = int(input('digite um numero: '))
numeros = (num1,num2,num3,num4)
pares = 0
print (numeros)
print (f'apareceram {numeros.count(9)} vez(es) o numero "9"')  

if numeros.index(3):
    print(f'o numero 3 apareceu pela primeira vez na pocição: {numeros.index(3) + 1}')

if num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0 or num4 % 2 == 0:
    pares += 1
print(f'teve {pares} numero(s) pare(s)')