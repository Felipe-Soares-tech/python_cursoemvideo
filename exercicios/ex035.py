print('+='*50)
print('Será que forma um triangulo?🧐')
print('+='*50)
a = float(input('qual o primeiro cumprimento? '))
b = float(input('qual o segundo cumprimento? '))
c = float(input('qual o terceiro cumprimento? '))
if a + b > c and a + c > b and b + c > a:
    print('essas 3 retas podem formar um triangulo')
else:
    print('essas 3 retas nao podem formar um triangulo')
