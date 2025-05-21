print ('Questão: Quando teve início a Revolução Francesa?')
print('a) 5 de maio de 1788')
print('b) 5 de maio de 1798')
print('c) 5 de maio de 1789')
print('d) nda')

x = str(input('Resposta:'))

if x == 'c':
    print ('Certa a resposta!')
else: 
    print('A reposta "{}" está errada.'.format(x))
    print('A alternativa correta é a "c".')
print('Fim!')