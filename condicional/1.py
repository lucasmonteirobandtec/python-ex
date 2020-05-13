from random import randint

nCpu = randint(0,5)

nUsr = int(input('Tente acertar o numero: '))

if nCpu != nUsr:
    print('Não acertou, tente novamente! CPU {} USER {}'.format(nCpu, nUsr))

else:
    print('Parabéns, você acertou! CPU {} USER {}'.format(nCpu, nUsr))