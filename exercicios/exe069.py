# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

idade = int(input('digite a idade da pessoa que vai ser cadastrada: '))
sexo = input('digite o sexo dessa pessoa "H" para homem e "M" para mulher: ').lower()
maiores = 0
homens = 0
mulher_menor = 0

while True:
    if idade > 18:
        maiores += 1
    
    if sexo == 'h':
        homens += 1
    
    if sexo == 'm' and idade < 20:
        mulher_menor += 1

    continuar = input('deseja continuar? S/N: ').lower()
    if continuar == 'n':
        break
    idade = int(input('digite a idade da pessoa que vai ser cadastrada: '))
    sexo = input('digite o sexo dessa pessoa "H" para homem e "M" para mulher: ').lower()

print(f''' tem {maiores} pessoas com mais de 18 anos,
    foram cadastrados {homens} homens
    e foram cadastradas {mulher_menor} mulheres com menos de 20 anos''')
