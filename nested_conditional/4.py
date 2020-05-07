age = int(input('Sua idade é: '))

if age == 18:
    print('Hora de se alistar')
elif age < 18:
    print('Ainda faltam {} anos para se alistar'.format(18 - age))
else:
    print('Já passaram {} anos para se alistar'.format(age - 18))
