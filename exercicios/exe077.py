# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# armazena as palavras em uma tupla
palavras = ('banana', 'borracha','messi','corvo','naruto','mark')
contagem = 0
verde = "\033[32m"  # Código ANSI para verde
reset = "\033[0m"   # Resetar a cor
vogal1 = 'a'
vogal2 = 'e'
vogal3 = 'i'
vogal4 = 'o'
vogal5 = 'u'
for i in palavras:
    print(i, end = ', ')
    print('vogais:')
    if vogal1 in palavras[contagem]:
        print(f'{verde}{vogal1}{reset}')

    if vogal2 in palavras[contagem]:
        print(f'{verde}{vogal2}{reset}')
    
    if vogal3 in palavras[contagem]:
        print(f'{verde}{vogal3}{reset}')
    
    if vogal4 in palavras[contagem]:
        print(f'{verde}{vogal4}{reset}')
    
    if vogal5 in palavras[contagem]:
        print(f'{verde}{vogal5}{reset}')

    contagem += 1


