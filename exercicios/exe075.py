# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:


# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

# for i in range(4):
#     num = int(input('digite um numero: '))

#para o usuario digitar os numeros
num1 = int(input('digite um numero: '))
num2 = int(input('digite um numero: '))
num3 = int(input('digite um numero: '))
num4 = int(input('digite um numero: '))

#armazena os numeros em uma tupla
numeros = (num1,num2,num3,num4)
pares = 0

print (numeros)

# escreve o quantas vezes apareceu o numero 9
print (f'apareceram {numeros.count(9)} vez(es) o numero "9"')  

# mostra em que posição aparece o numero 3 pela primeira vez
if 3 in numeros:
    print(f'o numero 3 apareceu pela primeira vez na pocição: {numeros.index(3) + 1}')
else:
    print('teve não numero 3 nao')


for i in numeros:
    if i % 2 == 0:
        pares += 1
print(f'teve {pares} numero(s) pare(s)')
