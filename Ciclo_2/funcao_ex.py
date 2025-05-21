print('Digite três notas de um aluno abaixo.')

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

def calcular_media ():
    n_final = (n1 + n2 + n3)/3
    print('Média final: {}'.format(n_final))

calcular_media ()
