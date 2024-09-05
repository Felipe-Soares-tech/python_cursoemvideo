frase = str(input('escreva uma frase: ')).strip().lower()
print('sua frase aparece {} vezes a letra A'.format(frase.count('a')))
print('a letra aparece a primeira vez na posição {}'.format(frase.find('a')+1))
print('e na ultima vez na posição {}'.format(frase.rfind('a')+1))


