# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
resposta = ''
while resposta != 'N':
    num = int(input('digite um numero: '))
    numeros.append(num)
    resposta = input('deseja digitar outra vez[S/N]? ').upper()
print(20*'=')
print(f'lista: {numeros}')

print(f'o tanto de numeros digitados: {len(numeros)}')

numeros.sort(reverse=True)
print(f'lista ordenada de forma decrescente: {numeros}')

print('Há o numero 5 na lista') if 5 in(numeros) else print('Não há o numero 5 na lista')