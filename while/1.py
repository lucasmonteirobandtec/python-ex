sex = str(input('Sexo: [M]/[F] ')).strip()[0]

while sex not in 'MnFf':
    sex = str(input('Digite novamente... [M]/[F] ')).strip()[0]

if sex in 'Mn':
    sex = 'masculino'
else:
    sex = 'feminino'

print('Sexo {} registrado com sucesso'.format(sex))