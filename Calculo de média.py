print('Informe a nota 1:')
N1 = float(input())
print('Informe a nota 2:')
N2 = float(input())
Me = (N1+N2)/2
if (Me>=6):
    print(f'Parabens, aprovado(a) com a media final {Me}')
else:
    print(f'Reprovado(a), média final {Me}')
