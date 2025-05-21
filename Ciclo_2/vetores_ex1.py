n = input('Digite os números do vetor separados por espaço: ')

vetor = [float(x) for x in n.split()]
escalar = float(input('Digite o escalar: '))
resultado = []

for componente in vetor:
    resultado.append(escalar*componente)

print('Resultado: ',resultado)