km = float(input('quantos kilometros seu carro alugado foi rodado? '))
dias = int(input(' e por quantos dias ele ficou alugado? '))
preço = dias*60+km*0.15
print ('o preço do seu carro rodado por {} km, alugado por {} dias é de {} R$'.format(km,dias,preço))

