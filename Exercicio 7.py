from random import randint

L = []
for a in range(10):
L.append(randint(1,50))

print(f'Lista não ordenada: {L}')
for i in range (len(L)):
for j in range (i+1,len(L)):
if (L[i]>L[j]):
temp=L[i]
L[i]=L[j]
L[j]=temp

print(f'Lista ordenada: {L}')