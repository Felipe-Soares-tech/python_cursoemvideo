# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input('qual foi sua primeira nota? '))
nota2 = float(input('qual foi sua segunda nota? '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'média: {media}, REPROVADO!')
elif 4.9 < media < 7:
    print(f'média: {media}, RECUPERAÇÃO!')
elif media > 6.9:
    print(f'média: {media}, APROVADO!')