import random
n1 = input('qual nome do aluno? ')
n2 = input('qual nome do aluno? ')
n3 = input('qual nome do aluno? ')
n4 = input('qual nome do aluno? ')
alunos = [n1,n2,n3,n4]
random.shuffle(alunos)

print('assim fica em ordem da lista dos alunos sorteados ')
print(alunos)