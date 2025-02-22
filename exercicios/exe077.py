# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# armazena as palavras em uma tupla
palavras = ('banana', 'borracha','messi','corvo','naruto','mark')
contagem = 0
vogal1 = 'a'
vogal2 = 'e'
vogal3 = 'i'
vogal4 = 'o'
vogal5 = 'u'
for i in palavras:
    print(i)
    print('vogais: ')
    if vogal1 in palavras[contagem]:
        print(f'{vogal1}, ')

    if vogal2 in palavras[contagem]:
        print(f'{vogal2}, ')

    if vogal3 in palavras[contagem]:
        print(f'{vogal3}, ')
    
    if vogal3 in palavras[contagem]:
        print(f'{vogal3}, ')
    
    if vogal4 in palavras[contagem]:
        print(f'{vogal4}, ')
    
    if vogal5 in palavras[contagem]:
        print(f'{vogal5}, ')

    contagem += 1






