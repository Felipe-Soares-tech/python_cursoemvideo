import random
import time
from time import sleep

jogadas = ['pedra', 'papel', 'tesoura']

python_jogada = random.choice(jogadas)

jogada = input('qual jogada voce tentará para me vencer? ').lower().strip()
print('sera que vc ganhou?')
sleep(1)

print(f'MINHA JOGADA FOI: {python_jogada}')

if jogada == 'pedra' and python_jogada == 'tesoura':
    print('voce ganhou!!!')
elif jogada == 'tesoura' and python_jogada == 'papel':
    print('voce ganhou!!!')
elif jogada == 'papel' and python_jogada == 'pedra':
    print('voce ganhou!!!')
else:
    print('voce perdeu!!!')