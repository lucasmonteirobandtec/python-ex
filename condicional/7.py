r1 = int(input('Digite o tamanho da reta 1: '))
r2 = int(input('Digite o tamanho da reta 2: '))
r3 = int(input('Digite o tamanho da reta 3: '))

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('Os segmentos podem formar um triangulo')
else:
    print('Os segmentos não podem formar um triangulo')