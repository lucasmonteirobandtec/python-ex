import random

user = int(input('Escolha entre: \n'
                 'Pedra - 1\n'
                 'Papel - 2\n'
                 'Tesoura - 3\n'))
cpu = random.randint(1,3)

if user < 1 or user > 3:
    print('Número inválido!')
else:
    if user == 1:
        user = 'pedra'
    if cpu == 1:
        cpu = 'pedra'
    if user == 2:
        user = 'papel'
    if cpu == 2:
        cpu = 'papel'
    if user == 3:
        user = 'tesoura'
    if cpu == 3:
        cpu = 'tesoura'

    if user == 'pedra' and cpu == 'pedra' or user == 'papel' and cpu == 'papel' or user == 'tesoura' and cpu == 'tesoura':
        print('DRAW! | you = {}, cpu = {}'.format(user, cpu))
    elif user == 'pedra' and cpu == 'tesoura' or user == 'papel' and cpu == 'pedra' or user == '3' and cpu == 'papel':
        print('YOU WINS | you = {}, cpu = {}'.format(user, cpu))
    else:
        print('YOU LOSE | you = {}, cpu = {}'.format(user, cpu))