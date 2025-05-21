print('Digite os coeficientes da função do segundo grau abaixo.')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if a == 0:
    print('Não é uma equação do segundo grau.')

else:
    delta = (b ** 2) - (4*a*c)

    if delta < 0:
        print('A equação não possui raízes reais.')
        
    elif delta > 0:
        x1 = (- b + delta)/(2*a)
        x2 = (- b - delta)/(2*a)
        print('Como delta é maior que zero, existem duas raízes distintas e reais: {} e {}'.format(x1,x2))

    elif delta == 0:
        x1 = (- b + delta)/(2*a)
        x2 = (- b - delta)/(2*a) 
        print('Como delta é igual a zero, existem duas raízes reais e iguais: {} e {}'.format(x1,x2))