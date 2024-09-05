import math
n = float(input('me diga um numero para mostrar seu seno coceno e tangente '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('seno é {:.2f}, cosseno é {:.2f}, e tangente é {:.2f}'.format(sen, cos, tan))


