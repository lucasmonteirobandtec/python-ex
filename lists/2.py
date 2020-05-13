li = []


while True:
    n = int(input('Digite um numero para coloca-lo na lista: '))
    if n not in li:
        li.append(n)
    n = str(input('Deseja continuar adicionando valores? [S/N] '))
    if n in 'Nn':
        break
li.sort()
print(li)
    