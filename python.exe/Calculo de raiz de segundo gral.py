import math
a = int(input('Digite o primeiro coeficiente: '))
b = int(input('Digite o segundo coeficiente: '))
c = int(input('Digite o terceiro coeficiente: '))

ds = (b*2) - 4 * (a * c)
if ds >= 0:
    x1 = (-b + math.sqrt(ds)) / (2 * a)
    x2 = (-b - math.sqrt(ds)) / (2 * a)
    print('Soluções: x1 = {}, x2 = {}'.format(x1, x2))
else:
    print('Não há soluções reais para essa equação.')