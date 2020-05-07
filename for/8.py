p = str(input('Digite uma frase: '))

p = p.replace(' ', '')
p = p.upper()
ip = p[::-1]
ip = ip.upper()


if p == ip:
    print('As palavras {} e {} são um Pálindromo'.format(p, ip))
else:
    print('As palavras {} e {} não são um Pálindromo'.format(p, ip))
