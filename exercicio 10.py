from random import randint
A = []

while(len(A)!=10):
x = randint(1,10)
if(x not in A):
A.append(x)

print(A)
