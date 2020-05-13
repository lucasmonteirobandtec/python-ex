fat = int(input('Digite um numero: '))
i = fat
print(fat, end = ' x ')

while i > 1:
    i -= 1
    fat = fat * i
    print(i, end=' = ' if i == 1 else ' x ')
print('{}'.format(fat))


for i in range(1, fat):
    fat = fat * i
print(fat)