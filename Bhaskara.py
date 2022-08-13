a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))

delta = (b**2) - 4*a*c

if a == 0:
    print("A deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** (1/2)) / (2*a)
    x2 = (-b - delta ** (1/2)) / (2*a)
    print("Delta: {}, x1: {}, x2: {}".format(delta,x1,x2))
