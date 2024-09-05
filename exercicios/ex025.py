nome = str(input('qual seu nome completo? ')).strip().upper().lower().capitalize()
#nome2 = 'silva'
correto = 'silva' in nome.lower()
print('seu nome tem silva? {}'.format(correto))
# meu a parte
if 'silva' in nome.lower():
   print('oh damn, this is fire!')
else:
   print('oh no man!')