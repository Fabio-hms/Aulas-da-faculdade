from random import randint

A = []
B = []
C = []
for i in range(20):
    A.append(randint(1,50))
    print(A)
for n in A:
    if(n%2==0):
        B.append(n)
    else:
        C.append(n)

print(f'Os valores pares: {B}')
print(f'Os valores impares: {C}')