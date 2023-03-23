print('Escreva o primeiro numero inteiro:')
N1 = int(input())
print('Escreva o segundo numero inteiro:')
N2 = int(input())
if(N1==N2):
    print('Os numeros são iguais!')
elif (N1>N2):
    print(f'Os numeros são diferentes e {N1} é maior que {N2}.')
elif (N2>N1):
    print(f'Os numeros são diferentes e {N2} é maior que {N1}.')

