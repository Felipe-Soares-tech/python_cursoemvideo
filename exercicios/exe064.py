# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = int(input('digite um numero inteiro: '))
contagem = 0
soma = 0

while num != 999:

    if num != 999:
        soma += num

    num = int(input('digite um numero inteiro: '))
    contagem += 1
    
print(f'''essa é a soma dos numeros que voce digitou: {soma}
e esse foi o tanto de vezes que voce digitou um número: {contagem}''')