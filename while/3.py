import time

n = 0

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))

while n != 5:
    n = int(input('[1] Somar\n'
                  '[2] Multiplicar\n'
                  '[3] Maior\n'
                  '[4] Novos numeros\n'
                  '[5] Sair do programa\n'))
    if n == 1:
        print('A soma dos numeros é: {}'.format(n1+n2))
    if n == 2:
        print('A multiplicação dos numeros é: {}'.format(n1*n2))
    if n == 3:
        if n1 > n2:
            print('O número {} é maior que o {} número'.format(n1, n2))
        else:
            print('O número {} é maior que o {} número'.format(n2, n1))
    if n == 4:
        n1 = int(input('Digite o 1º numero: '))
        n2 = int(input('Digite o 2º numero: '))
    time.sleep(1)

print('Você saiu do programa')