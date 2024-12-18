# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
palpites = 0
chute = 11
numero = 0
while chute != numero:
    chute = int(input('escolha um numero de 1 a 10: '))
    numero = randint(1,10)
    print('processando...')
    sleep(1)
    print('$'*20)

    if chute == numero:
        print('voce ganhou!')
        palpites += 1
    else:
        print('voce perdeu :( , tente novamente!')
        palpites += 1

print(f'foram necessarios {palpites} para o acerto!')
