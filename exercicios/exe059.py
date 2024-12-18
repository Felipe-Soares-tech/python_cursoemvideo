# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = int(input('digite um valor inteiro: '))
valor2 = int(input('digite outro valor inteiro: '))

print('''[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa''')
print('-'*40)

acao = 0

while acao != 5:
    acao = int(input('que ação voce deseja executar? '))
    print('-'*40)
    match acao:
        case 1:
            soma = valor1 + valor2
            print(f'a soma dos valores "{valor1}" e "{valor2}" é: {soma}')

        case 2:
            multi = valor1 * valor2
            print(f'a multiplicação dos valores "{valor1}" e "{valor2}" é: {multi}')
        case 3:
            if valor1 > valor2:
                print(f'o primeiro valor "{valor1}" é maior do que o segundo "{valor2}"')
            elif valor2 > valor1:
                print(f'o segundo valor "{valor2}" é maior do que o primeiro "{valor1}"')
        case 4:
            valor1 = int(input('digite um valor inteiro: '))
            valor2 = int(input('digite outro valor inteiro: '))




