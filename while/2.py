from random import randint

num = int(input('Digite um numero de 1 a 10: '))
num2 = randint(0, 10)

while num != num2:
    num2 = randint(0, 10)
    num = int(input('Digite um numero de 1 a 10: '))

print('Você acertou')