li = []
while True:
    n = int(input('Numero: '))
    li.append(n)
    
    c = str(input('Continuar? [S/N] '))
    if c in 'Nn':
        break

print(len(li))

li.sort(reverse=True)
print(li)

if 5 in li:
    print('5 está na lista')
else:
    print('5 não está na lista')