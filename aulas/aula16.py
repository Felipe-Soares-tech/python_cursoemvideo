lanche = ('pizza', 'hamburguer','suco')
print(lanche)

for i in lanche:
    print(i)


print(lanche[2])

print(len(lanche))

for i in range(0, len(lanche)):
    print(f'vou comer {lanche[i]}, na posição {i}')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao+1}')