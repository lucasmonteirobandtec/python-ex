lista = []
for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for i in range(5):
            if n <= lista[i]:
                lista.insert(i,n)
                break
print(lista)