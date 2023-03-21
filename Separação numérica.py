print('Digite um numero de até 3 digitos:')
N = int(input())
C = N//100
D = (N%100)//10
U = (N%100)%10
print(f'A centena é {C}, a dezena é {D}, a unidade é {U}')
