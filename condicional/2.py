v = int(input('Digite sua velocidade: '))

if (v > 80):
    print('Foi multado em R${:.2f}'.format(7*(v - 80)))
