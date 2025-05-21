print('Digite os valores dos três lados do triâgulo.')
a = float(input('Lado a = '))
b = float(input('Lado b = '))
c = float(input('Lado c = '))

if a == b == c:
    print('O triâgulo é equilátero.')

elif a != b != c:
    print ('O triângulo é escaleno.')

else:
    print ('O triângulo é isósceles.')

print('Fim!')