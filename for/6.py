x1 = int(input('Digite o primero termo da PA: '))
xr = int(input('Digite a razao da PA: '))
xn = x1 + (10 - 1) * xr


for i in range(x1, xn, xr):
    print('{}'.format(i), end=' => ')
print('DONE!')
