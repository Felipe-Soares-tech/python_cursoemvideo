# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input('digite um numero inteiro: '))
contagem = 0
soma = 0
maior = 0
menor = 0
mais_num = ''
while mais_num != 'n':
    if contagem == 0:
        menor = num
    contagem += 1
    soma += num
    if num > maior:
        maior = num
    
    elif num < menor:
        menor = num
    
    media = soma/contagem

    mais_num = input('deseja digitar mais números? S/N: ').lower()
    if mais_num == 'n':
        break
    num = int(input('digite um numero inteiro: '))
    

print(f'''seu maior numero foi: {maior}
e seu menor numero foi: {menor}''')
