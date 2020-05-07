fat = int(input('Digite um numero: '))
i = fat

while i > 1:
    i -= 1
    fat = fat * i
print(fat)


for i in range(1, fat):
    fat = fat * i
print(fat)
