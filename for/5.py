s = 0
for i in range(6):
    n = int(input('Digite o {}º numero: '.format(i + 1)))
    if n % 2 == 0:
        s += n
print(s)
