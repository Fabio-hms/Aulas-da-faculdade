from random import randint

A = []
x = int(input("Digite um valor: "))
pertence = 0

for i in range(10):
    A.append(randint(1,50))

for n in A:
    if(n==x):
        pertence += x

    if(x==pertence):
        print(f'O numero {pertence} está na lista {A}')
    else:
        print(f'O numero {pertence} não está na lista {A}')