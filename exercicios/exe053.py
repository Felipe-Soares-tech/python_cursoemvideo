palavra = input('digite uma palavra ou frase qualquer: ').strip()

if palavra[::-1] == palavra:
    print(f' {palavra} é um palíndromo')
else:
    print(f'{palavra} não é um palíndromo')





