i = 1
li = []

while i <= 3:
    li.append(int(input('{} segmento:'.format(i))))
    i += 1

if li[0] < li[1] + li[2] and li[1] < li[0] + li[2] and li[2] < li[0] + li[1]:
    print('Pode ser um triangulo')
    if li [0] == li [1] == li [2]:
        print('É um triângulo EQUILÁTERO')
    elif li[0] == li[1] or li[1] == li[2] or li[2] == li[0]:
        print('É um triângulo ISÓSCELES')
    else:
        print('É um triângulo ESCALENO')
else:
    print('Não pode formar um triângulo')
