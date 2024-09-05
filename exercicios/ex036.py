valor = float(input('qual o valor desta casita? '))
salario = float(input('qual seu salario atual? '))
anos = int(input('em quantos anos vc vai pagar a casita? '))
import time

# percentage: Por exemplo, se você quer calcular 35% de 500, multiplique 35 por 500
# Fazendo isso você obtém o valor de 35 x 500 = 17500; Divida o resultado obtido por 100.
prestation = valor / (anos * 12)

print(
    'para voce conseguir o emprestimo o valor da sua casa, R${:.2f} tem que ter a prestação menor que 30% do seu salario'.format(
        valor))
porcentation = salario * 30 / 100

if prestation > porcentation:
    print('=+' * 50)
    print('calculating...')
    time.sleep(3)
    print('emprestimo negado! sua prestação de {} excedeu os 30%'.format(prestation))
else:
    print('=+' * 50)
    print('calculating...')
    time.sleep(3)
    print('emprestimo concedido, ce é fera boy')
