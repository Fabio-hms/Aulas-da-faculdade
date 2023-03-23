#Programa simples, apenas para praticar a logica de programação, esse tipo de calculo deve levar em consideração
#diversas informações a mais.
print('Informe seu Sexo M(Masculino) ou F(Feminino):')
Se=(input())
if(Se == 'M'):
    print('Informe sua altura:')
    Alt = float(input())
    Ph=(72.7*Alt)-58
    print(f'Seu peso ideal é {Ph}')
elif(Se == 'F'):
    print('Informe sua altura:')
    Alt = float(input())
    Pf=(62.1*Alt)-44.7
    print(f'Seu peso ideal é {Pf}')
elif(Se!= 'M' and Se!='F'):
    print('Não existe peso ideal.')