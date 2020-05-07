trip = int(input('Qual a distancia da viagem?\n'))

if(trip > 200):
    print('O preco será de R${}'.format((45/100)*trip))
else:
    print('O preco será de R${}'.format((50/100)*trip))