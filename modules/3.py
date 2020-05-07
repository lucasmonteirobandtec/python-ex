import math

an = int(input("Digite o ângulo que você deseja: "))

if (an == 90 or an == 270):
    tan = 0

sin = math.sin(math.radians(an))
cos = math.cos(math.radians(an)) 
tan = math.tan(math.radians(an))

print("O angulo {} tem o SENO de {:.2f}".format(an, sin))
print("O angulo {} tem o COSSENO de {:.2f}".format(an, cos))
print("O angulo {} tem a TANGENTE de {:.2f}".format(an, tan))
