n = int(input('Digite um número: '))
contar_primos = 0

while n > 1:
    divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            divisores += 1
        i += 1
    if divisores == 2:
        contar_primos += 1
    n -= 1

print('A quantidade de primos encontrados é: {}'.format(contar_primos))