value = int(input('O valor da casa: '))
salary = int(input('O valor do seu salário: '))
year = int(input('Quantos anos ele vai pagar?\n'))

installment = value / (year * 12)

if installment > salary * 30/100:
    print('Emprestimo foi negado')
else:
    print('Emprestimo foi aprovado')