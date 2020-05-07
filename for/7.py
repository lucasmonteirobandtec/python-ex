n = int(input('Digite um numero: '))

for i in range(1, n):
    if n % i != 0:
        print('é primo {}'.format(i))
    else:
        print('não é primo {}'.format(i))