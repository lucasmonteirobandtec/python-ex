n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))
n4 = int(input('Digite outro numero: '))
t = (n1, n2, n3, n4)

print(f'O 9 apareceram: {t.count(9)} vezes')
print(f'O 3 apareceu na: {t.index(3)} posição')

for n in t:
    if n % 2 == 0:
        print(f'Os numeros pares são: {n}')