sumAge = 0
avgAge = 0
ageOldM = 0
nameOldM = ''
qntW = 0

for i in range(4):
    name = str(input('Digite um nome: '))
    age = int(input('Digite uma idade: '))
    sex = str(input('Digite o sexo:\n'
                    'Feminino - F\n'
                    'Masculino - M\n'))
    sumAge += age
    if sex in 'Mm':
        if i == 1:
            ageOldM = age
            nameOldM = name
        else:
            if ageOldM < age:
                ageOldM = age
                nameOldM = name
    else:
        if age < 20:
            qntW += 1

avgAge = sumAge / i

print('A idade média do grupo é {}'.format(avgAge))
print('O nome do homem mais velho é {}'.format(nameOldM))
print('Existem {} mulheres abaixo de 20 nesse grupo'.format(qntW))
