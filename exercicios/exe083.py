# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses abertos e fechados na ordem correta.

expressao = list(input('digite uma expressão qualquer: '))
ler = len(expressao)
parenteses = 0
pos = 0

if (expressao.count('(') + expressao.count(')'))% 2 == 0:
    print('válida sua expressão')
else:
    print('inválida sua expressão')

