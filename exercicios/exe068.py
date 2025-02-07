# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

num = int(input('digite um numero: '))
jogada = input('escolhe Impar ou Par? I/P: ').lower()
soma = 0
random2 = ''

while True:
    random1 = random.randint(1,30)
    print(f'meu numero é: {random1}')

    if jogada == 'i':
        random2 = 'P'
        print(f'minha jogada é: {random2}')
    else:
        random2 = 'I'
        print(f'minha jogada é: {random2}')


    soma = num + random1

    if soma % 2 == 0 and random2 == 'P':
        print('VOCE PERDEEEEEEU !!!!!')
        break
    elif soma % 2 != 0 and random2 == 'I':
        print('VOCE PERDEEEEEEU !!!!!')
        break
    else:
        print('voce ganhou! jogue novamente')

    num = int(input('digite um numero: '))
    jogada = input('escolhe Impar ou Par? I/P: ').lower()

    



