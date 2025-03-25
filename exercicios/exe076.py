# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# lista e produtos e devidos preços dentro de uma tupla em uma variavel
listagem = ('nutella', 25, 'tesla', 400, 'laranja', 20, 'mentos', 15, 'pamonha', 500)


# listando produtos e preços em uma tabela tipo nota fiscal
for i in range(0, len(listagem)):

    # se a posição dividida por 2 for igual a zero ele printa
    if i % 2 == 0:
        print(f'{listagem[i]}', end=''), print((30 - len(listagem[i])) * '.', end='')
    
    # mesma coisa so que ao contrario
    if i % 2 != 0:
        print(f'R${listagem[i]}')