pvJinx = int(input("Digite a vida da Jinx: "))
pvEkko = int(input("Digite a vida da Ekko: "))
n = int(input("Digite a quantidades de ataques da Jinx: "))

for i in range(n):
    AtJ = int(input("Digite a quantidade de dano do ataque da Jinx: "))
    if (pvJinx != 0):
        if (pvJinx < pvEkko):
            AtJ //=2
        pvEkko -= AtJ
        if(pvEkko < 0):
            pvEkko = 0

n1 = int(input("Digite a quantidades de ataques do Ekko: "))
for j in range(n1):
    AtE = int(input("Digite a quantidade de dano do ataque do Ekko: "))
    if (pvEkko != 0):
        if(pvEkko < pvJinx):
            AtE //= 2
        pvJinx -= AtE
        if (pvJinx < 0):
            pvJinx = 0

if(pvEkko > pvJinx):
    print(f'Ekko ganhou!, Ekko ficou com {pvEkko} de vida restante, Jinx perdeu, com a vida de {pvJinx}')
elif(pvJinx > pvEkko):
    print(f'Jinx ganhou! Jinx ficou com {pvJinx} de vida restante, Ekko perdeu, com a vida de {pvEkko}')
else:
    print(f'Empatou! Ekko ficou com {pvEkko} de vida restante e Jinx ficou com {pvJinx} de vida restante ')