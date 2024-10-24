# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se
# alistar ou se já passou do tempo do alistamento. Seu programa também
# deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('qual sua idade? '))

if idade == 18:
    print('está na hora EXATA de voce se alistar!')
elif idade > 18:
    print(f'''já passou da hora de voce se alistar, 
e faz {idade - 18} ano(s) que voce tinha que ter se alistado ''')
elif idade < 18:
    print(f'ainda faltam {18 - idade} anos para voce se alistar')

