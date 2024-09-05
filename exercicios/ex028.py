from random import randint
from time import sleep
chute = int(input('escolha um numero de 1 a 10: '))
numero = randint(1,10)
print('processando...')
sleep(2)
print('$'*20)
if chute == numero:
    print('voce ganhou!')
else:
    print('voce perdeu :( era {}'.format(numero))
