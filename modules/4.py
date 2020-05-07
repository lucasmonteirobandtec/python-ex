import random

i = 0

li = [] 

while i < 5:
    name = input("Digite um nome: ")
    li.append(name)
    i += 1

random.shuffle(li)

print("A ordem de apresentação será: {}".format(li))