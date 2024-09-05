chute = str(input('diga a cidade que voce mora: ')).strip().upper().lower().capitalize()
# armazena o a cidade que voce mora
city = 'Taguatinga'
# a cidade que o programa
correto = city in chute
print(correto)
if city in chute:
      print('your city is taguatinga!')
else:
      print('your city is not taguatinga!')
