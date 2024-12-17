# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
maior = 0
nome_older = ''
for i in range(1,5):
    nome = input('qual seu nome? ')
    idade = (int(input('quantos anos voce tem? ')))
    sexo = input('qual seu sexo?(COLOQUE "F" PARA FEMININO E "M" PARA MASCULINO ')
    soma += idade
    if i == 1 or idade > maior:  # Primeira pessoa ou nova maior idade
        maior = idade
        nome_older = nome  # Armazena o nome da pessoa mais velha


print(f'''a média de idade do grupo é {soma/4}.
O nome da pessoa mais velha é {nome_older},{maior}''')