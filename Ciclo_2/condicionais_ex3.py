num = int(input('Digite seu número USP:'))
num_str = str(num)
segundo_digito = int(num_str[1])

if segundo_digito == 7:
    print('Você entrou na USP em 2025.')

elif segundo_digito == 6:
    print('Você entrou na USP em 2024.')

elif segundo_digito == 5:
    print('Você entrou na USP em 2023.')

elif segundo_digito == 4:
    print('Você entrou na USP em 2022.')

elif segundo_digito == 3:
    print('Você entoru na USP em 2021.')

elif segundo_digito == 2:
    print('Você entrou na USP em 2020.')

elif segundo_digito >= 8:
    print('Provavelmente, se refere a anos posteriores.')

else:
    print('Veterano demais.')