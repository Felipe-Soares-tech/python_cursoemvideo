import random
n1 = input('qual o nome do aluno? ')
n2 = input('qual o nome do aluno? ')
n3 = input('qual o nome do aluno? ')
n4 = input('qual o nome do aluno? ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('{}'.format(escolhido))

