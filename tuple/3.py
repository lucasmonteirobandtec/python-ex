from random import randint

r = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

for n in r:
    print(n)

print(f'O max numero foi {max(r)}')
print(f'O min numero foi {min(r)}')