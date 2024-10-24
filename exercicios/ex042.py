print('+='*50)
print('Será que forma um triangulo?🧐')
print('+='*50)
a = float(input('qual o primeiro cumprimento? '))
b = float(input('qual o segundo cumprimento? '))
c = float(input('qual o terceiro cumprimento? '))
if a + b > c and a + c > b and b + c > a:
    print('essas 3 retas podem formar um triangulo')
    if b == a == c:
        print(f'os lados do seu triangulo {a}, {b}, {c} sao iguais, então é EQUILÁTERO')
    elif b == a or b == c or a == c:
        print('dois lados do seu triangulo sao iguais, ISÓSCELES')
    elif b != a != c:
        print('todos os lados sao diferentes, ESCALENO')
else:
    print('essas 3 retas nao podem formar um triangulo')

