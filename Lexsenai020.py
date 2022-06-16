maiori=[]
menori=[]
num=int(input('Digite sua idade:'))
if num>=18:
            maiori.append(num)
            qtdmaior=len(maiori)
elif  num<=17 and num>0:
            menori.append(num)
            qtdmenor=len(menori)
while num>0:
    num=int(input('Digite sua idade:'))
    if num>=18:
            maiori.append(num)
            qtdmaior=len(maiori)
    elif  num<=17 and num>0:
            menori.append(num)
            qtdmenor=len(menori)
print('A quantidade de pessoas menores de idade é:',qtdmenor)
print('A quantidade de pessoas maiores de idade é:',qtdmaior)

