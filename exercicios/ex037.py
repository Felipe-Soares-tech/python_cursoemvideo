
numero = int(input('digite um numero inteiro: '))

print(''' OPÇÕES:
[ 1 ] para converter para BINARIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL''')

opcao = int(input('escolha sua opção: '))
while opcao > 3 or opcao < 1:
    print('erro')
    opcao = int(input('escolha sua opção: '))
match opcao:
    case 1:
        print(f'{numero} em binario é {bin(numero)[2:]}')
    case 2:
        print(f'{numero} em octal é {oct(numero)[2:]}')
    case 3:
        print(f'{numero} em hexadecimal é {hex(numero)[2:]}')
    case _:
        print('NÃO')

