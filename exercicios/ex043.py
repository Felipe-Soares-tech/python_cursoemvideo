# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

peso = float(input('qual seu peso? '))
altura = float(input('qual sua altura? '))


imc = peso/(altura * altura)

if imc < 18.5:
    print(f'seu imc: {imc:.2f} abaixo de 18.5, voce está abaixo do peso')
elif 18.4 < imc < 24.99:
    print(f'seu imc: {imc:.2f} está Entre 18,5 e 25 , voce está no peso ideal')
elif  24.99 < imc < 29.99:
    print(f'seu imc: {imc:.2f} está Entre 25 e 30 , voce está sobrepeso')
elif 29.99 < imc < 39.99:
    print(f'seu imc: {imc:.2f} está Entre 30 e 40 , voce está obeso')
elif imc > 39.99:
    print(f'seu imc: {imc:.2f} acima de 40, voce está com obesidade mórbida')
