from time import sleep
dis = float(input('what is your travel distance? '))
if dis <= 200:
    preço = 0.50*dis
    print('the price is calculated 0,50R$ per each KM')
    print('calculating...')
    sleep(2)
    print(f'your travel is less than 200KM so the price is {preço}')
else:
    preço2 = 0.45*dis
    print('the price is calculated 0,45R$ per each KM')
    print('calculating...')
    sleep(2)
    print(f'your travel is more than 200KM so the price is {preço2}')

