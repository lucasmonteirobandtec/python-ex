big = 0
sma = 0
for x in range(5):
    w = float(input('Digite um peso: '))
    if x == 1:
        big = w
        sma = w
    else:
        if w > big:
            big = w
        if w < sma:
            sma = w
print('O maior peso foi de {} e o menor de {}'.format(big, sma))