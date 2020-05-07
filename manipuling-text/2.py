n = int(input("Digite um numero de 0 a 9999: "))

# estudar sobre modulação

u = n // 1 % 100
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print("unidade: {}".format(u))
print("dezena: {}".format(d))
print("centena: {}".format(c))
print("milhar: {}".format(m))