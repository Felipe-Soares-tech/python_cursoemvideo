valores = []

while True:
    num = int(input("Digite um número: "))
    
    if num not in valores:
        valores.append(num)
        print("Número adicionado com sucesso!")
    else:
        print("Número duplicado! Não será adicionado.")
    
    continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print(f"Os valores únicos digitados em ordem crescente são: {sorted(valores)}")