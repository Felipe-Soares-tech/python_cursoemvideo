# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = ''
while sexo != 'f' and sexo != 'm':
    sexo = input('qual seu sexo [f/m]? ').lower()