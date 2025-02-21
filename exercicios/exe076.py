# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

<<<<<<< HEAD
listagem = ('sapato',90, 'maçã', 1, 'melão', 5, 'alcatra', 100, 'nutella', 25)

for item in listagem:
    print(item)
=======
# lista e produtos e devidos preços dentro de uma tupla em uma variavel
listagem = ('nutella', 25, 'tesla', 400, 'laranja', 20, 'mentos', 15, 'pamonha', 500)
def conta(x):
    conta2 = len(listagem[x])

#
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]}', end=''), print((30 - len(listagem[i])) * '.', end='')
    
    if i % 2 != 0:
        print(f'R${listagem[i]}')
>>>>>>> f14982a625394f40968066895e4af315df31a5b2
