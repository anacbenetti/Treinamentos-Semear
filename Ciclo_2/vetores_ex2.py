n = input('Digite os números do vetor 1 separados por espaço: ')
m = input('Digite os números do vetor 2 separados por espaço: ')

vetor1 = [float(x) for x in n.split()]
vetor2 = [float(y) for y in m.split()]

if len(vetor1) != len(vetor2):
    print('Os vetores devem ter o mesmo número de componentes!')

else:
    print('Para somar os vetores, digite 1. Para multiplicá-los, digite 2.')
    O = int(input())

    if O == 1:
        resultado1 = [vetor1[i] + vetor2[i] for i in range(len(vetor1))]
        print('Esse é o vetor resultante: ', resultado1)

    elif O == 2:
        resultado2 = [vetor1[i] + vetor2[i] for i in range(len(vetor1))]
        print('Esse é o vetor resultante: ', resultado2)