print('Digite dois números abaixo.')
x = float(input('Número 1: '))
y = float(input('Número 2: '))

if x == y:
    print('Os números são iguais.')

elif x > y:
    print('O maior número é {}'.format(x))

elif x < y:
    print('O maior número é {}'.format(y))