# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

valores = []
num = 0


for i in range(0,5):
    num = int(input('digite um numero: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)  
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1

    
print(valores)