import math

cop = int(input("Comprimento do cateto oposto: "))
cad = int(input("Comprimento do cateto adjacente: "))

hi = math.sqrt((cop**2)+(cad**2))

print ("A hipotenusa vai medir {}".format(hi))