from datetime import date
chute = int(input('say a year '))
if chute == 0:
    chute = date.today().year
if chute % 4 == 0 and chute % 100 != 0 or chute % 400 == 0:
    print(f'your year {chute} is leap')
else:
    print(f'your year {chute} is not leap')
