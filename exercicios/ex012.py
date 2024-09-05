price = float(input('qual é o preço do produto? '))
desconto = (price*5)/100
nprice = price - desconto
print('o produto mais o desconto de 5% fica {}'.format(nprice))