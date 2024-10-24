idade = int(input('qual a idade do atleta? '))

if idade < 10:
    print(f'''idade: {idade} 
categoria: MIRIM''')
elif 9 < idade < 15:
    print(f'''idade: {idade}
categoria: INFANTIL''')
elif  14 < idade < 20:
    print(f'''idade: {idade}
categoria: JUNIOR ''')
elif 19 < idade < 26:
    print(f''' idade: {idade}
categoria: SÊNIOR''')
elif idade > 25:
    print(f'''idade: {idade}
categoria: MASTER''')