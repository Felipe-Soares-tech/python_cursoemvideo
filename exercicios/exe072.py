# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
            'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
            'dezoito', 'dezenove', 'vinte')

numero = int(input("Digite um número entre 0 e 20: "))

# Verifica se o número está no intervalo correto

if 0 <= numero <= 20: 
    print(F'SEU NUMERO POR EXTENSO É: {contagem[numero]}')