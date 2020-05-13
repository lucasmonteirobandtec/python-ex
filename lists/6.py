exp = str(input('Digite a sua expressao: '))

li = []

for s in exp:
    if s == '(':
        li.append(s)
    elif s == ')':
        if len(li) > 0:
            li.pop()
        else:
            li.append(s)
            break
if len(li) > 0:
    print('Expressão inválida')
else:
    print('Expressão válida')