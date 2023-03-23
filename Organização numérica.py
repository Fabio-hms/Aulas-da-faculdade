print('Informe um valor para A:')
A = int(input())
print('Informe um valor para B:')
B = int(input())
print('Informe um valor para C:')
C = int(input())
if(A>B and A>C):
    print(f'A é o maior valor entre A, B e C: {A}, {B}, {C}')
elif (B>A and B>C):
    print(f'B é o maior valor entre A, B e C: {A}, {B}, {C}')
elif (C>A and C>B):
    print(f'C é o maior valor entre A, B e C: {A}, {B}, {C}')

