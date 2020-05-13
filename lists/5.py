li = []
liPar = []
liImpar = []

while True:
    n = int(input('Numero: '))
    li.append(n)
    if n % 2 == 0:
        liPar.append(n)
    else:
        liImpar.append(n)
    s = str(input('Continuar? [S/N]'))
    if s in 'Nn':
        break
print(li)
print(liPar)
print(liImpar)