# Por exemplo, se você quer calcular 35% de 500, multiplique 35 por 500.
# Fazendo isso você obtém o valor de 35 x 500 = 17500; Divida o resultado obtido por 100


valor = int(input('qual o valor desse produto? '))

print(f'''[1] à vista no cartão: 5% de desconto
[2] em até 2x no cartão: preço formal
[3] 3x ou mais no cartão: 20% de juros''')

desconto = (5 * valor) / 100
juros = (20 * valor) / 100
opcao = int(input('escolha uma opção de pagamento: '))
match opcao:
    case 1:
        print(f'como voce escolheu pagar a vista voce ganhou 5% de desconto, logo o preço ficará R${valor - desconto}')
    case 2:
        print('o preço não vai ser alterado')
    case 3:
        print(f'o preço será afetado com juros e ficará R${valor + juros}')
    case _:
        print('INVÁLIDO')

