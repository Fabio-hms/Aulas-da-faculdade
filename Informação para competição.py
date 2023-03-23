print('informe a idade do competidor:')
Id=int(input())
if(Id<=8):
    print('Categoria infantil A')
elif(Id<13):
    print('Categoria infantil B')
elif(Id<18):
    print('Categoria juvenil A')
elif(Id<21):
    print('Categoria juvenil B')
elif(Id>=21):
    print('Categoria senior')