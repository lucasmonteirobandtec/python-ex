li = []

for i in range(7):
    li.append(int(input('Digite uma idade: ')))

for age in li:
    if age < 18:
        print('{} é menor de idade'.format(age), end=' -> ')
    else:
        print('{} é maior de idade'.format(age), end=' -> ')
print('FIM')
