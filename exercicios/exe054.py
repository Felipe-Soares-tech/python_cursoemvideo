for i in range(7):
    ano = int(input('diga que ano voce nasceu: '))
    if ano < 2006:
        print('\033[32m')#menor de idade
    elif ano > 2006:
        print('\033[31m')#maior de idade
    else:
        print('\033[34m')
    print(i, end=' ')



