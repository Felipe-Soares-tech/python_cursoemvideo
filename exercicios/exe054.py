#  Crie um programa que leia o ano de nascimento de sete pessoas. 
#  No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior = 0
menor = 0
for i in range(7):
    ano = int(input('em que ano voce nasceu? '))
    if ano <= 2006:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas são maiores de idade')
print(f'{menor} pessoas são menores de idade')






