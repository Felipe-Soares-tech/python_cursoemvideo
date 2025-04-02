lista = []
maior = 0
menor = 0
num = 0

for i in range(1, 6):
    num = int(input('Digite um número: '))
    lista.append(num)
    print(num)

    # Atualiza 'maior' corretamente
    maior = num if num > maior else maior

    # Atualiza 'menor' corretamente (tratando o primeiro número)
    menor = num if i == 1 else (num if num < menor else menor)

print(f'''A lista: {lista}
Maior elemento: {maior}
Menor elemento: {menor}''')