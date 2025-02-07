# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

nome = input('qual o nome do produto? ')
preco = float(input('qual o preço do produto? '))
total = 0
mais_mil = 0
mais_barato = ''
mais_barato2 = 0
cont = 0
while True:
    cont += 1
    if cont == 1:
        mais_barato2 += preco 

    total += preco
    
    if preco > 1000:
        mais_mil += 1
    
    if preco < mais_barato2:
        mais_barato2 = preco
        mais_barato = nome
    
    continuar = input('deseja continuar? S/N: ').lower()
    if continuar == 'n':
        break
    nome = input('qual o nome do produto? ')
    preco = float(input('qual o preço do produto? '))

print(f'''O total gasto na compra foi de R${total},
{mais_mil} produtos custaram mais de R$1000
e o produto {mais_barato} é o mais barato com R${mais_barato2}.''')

    
