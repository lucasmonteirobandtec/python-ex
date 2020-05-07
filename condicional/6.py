salary = float(input('Digite seu salario: '))

if(salary > 1250.00):
    print('Você receberá um aumento de 10% e seu novo salario sera{}'.format(salary+(salary*(15/100))))
else:
    print('Você receberá um aumento de 15% e seu novo salario será de:{}'.format(salary+(salary*(15/100))))