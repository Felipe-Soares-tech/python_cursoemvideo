# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:


# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

times = ("Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo", "RB Bragantino", 
         "Fluminense", "Athletico-PR", "Internacional", "Fortaleza", "São Paulo", "Cuiabá", 
         "Corinthians", "Cruzeiro", 
         "Vasco", "Bahia", "Santos", "Goiás", "Coritiba", "América-MG")
print('Os 5 primeiros times.')
for posicao,time in enumerate(times[0:5]):
    print(posicao+1,time)
print('=*'*30)

print('Os últimos 4 colocados.')
for posicao,time in enumerate(times[19:15:-1]):
    print(posicao+17,time)
print('=*'*30)

print('Times em ordem alfabética.')
for time in sorted(times):
    print(time)
print('=*'*30)

print('Em que posição está o time do Flamengo.')

for posicao, time in enumerate(times):
    if time == 'Flamengo':
        print(f'o time {time}, está na {posicao+1} posição')
    
    # print(posicao, time)

    