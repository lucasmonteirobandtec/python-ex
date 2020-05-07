num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num1 < num2:
    print('{} é menor que {}'.format(num1, num2))
else:
    print('{} é igual a {}'.format(num1, num2))