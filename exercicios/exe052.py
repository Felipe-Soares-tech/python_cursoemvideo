num = int(input('digite um numero: '))
total = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{i}',end=' ')

if total == 2:
    print('\n seu numero é primo')
else:
    print('\n seu numero nao é primo')