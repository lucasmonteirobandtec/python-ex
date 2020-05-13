people = list()
person = list()
weightMax = weightMin = 0


while True:
    person.append(str(input('Nome: ')))
    person.append(int(input('Peso: ')))
    if len(people) == 0:
        weightMax = weightMin = person[1]
    else:
        if person[1] < 85:
            weightMin = person[1]
        else:
            weightMax = person[1] 
    people.append(person[:])
    person.clear()
    s = str(input('Deseja continuar? '))
    if s in 'Nn':
        break
print(f'{len(people)} pessoas foram cadastradas')
print(f'O maior peso foi de {weightMax}, de:', end=' ')
for p in people:
    if p[1] == weightMax:
        print(f'{p[0]}', end=' ') 
print()
print(f'O menor peso foi de {weightMin}, de:', end=' ')
for p in people:
    if p[1] == weightMin:
        print(f'{p[0]}', end=' ')
print()