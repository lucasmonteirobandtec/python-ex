t = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez' , 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um numero de 1 à 20: '))

while n < 0 or n > 20:
    n = int(input('Digite novamente um numero de 1 à 20: '))

print(t[n])