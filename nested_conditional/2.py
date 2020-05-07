num = int(input('Numero que deseja converter: '))

case = int(input('1 - binario\n'
                 '2- octal\n'
                 '3 - hexadecimal\n'))

if case == 1:
    print('{} é igual a {} em binário'.format(num, bin(num)))
elif case == 2:
    print('{} é igual a {} em octal'.format(num, oct(num)))
else:
    print('{} é igual a {} em hexadecimal1'.format(num, hex(num)))