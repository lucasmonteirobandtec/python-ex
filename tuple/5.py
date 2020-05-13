li = ('Pão', 1,
 'Frango', 10,
 'Veja', 12,
 'Caderno', 39.90,
 'Lápis', 10.90)

print('-' * 30)
print(f'{"Lista de Compras":^30}')
print('-' * 30)

for c in range(0, len(li)):
    if c % 2 == 0:
        print(f'{li[c]:.<15}', end='')
    else:
        print(f'{li[c]:.>15.2f}')
print('-' * 30)
