print('Informe o saldo da sua conta:')
Sa = float(input())
print('Informe a quantidade a ser sacada:')
Re = float(input())
if (Re <= Sa):
    print('Retire as cedulas abaixo!')
else:
    print('Saldo insulficiente!')