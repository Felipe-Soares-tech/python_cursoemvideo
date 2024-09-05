from math import hypot
co = float(input('qual o comprimento do cateto oposto deste triangulo? '))
ca = float(input('qual o comprimento do cateto adjacente deste triangulo? '))
hi = hypot(ca, co)
print('o valor é {:.2f}'.format(hi))
