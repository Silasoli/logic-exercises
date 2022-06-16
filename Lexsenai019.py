par=[]
impar=[]
lisnum=[]
num=int(input('Digite um número:'))
lisnum.append(num)
while num>0 and num!=0:
    num=int(input('Digite um número:'))
    lisnum.append(num)
for num in lisnum:
        if num % 2==0:
            par.append(num)
        else:
            impar.append(num)

somapar=sum(par)
qtdpar=len(par)
qtdpar2=qtdpar-1
medpar=somapar/qtdpar2
print('A média de números pares é:', medpar)

somaim=sum(impar)
qtdim=len(impar)
medim=somaim/qtdim
print('A média de números impares é:', medim)

somatt=sum(lisnum)
qtdtt=len(lisnum)
qtdtt2=qtdtt-1
medtt=somatt/qtdtt2
print('A média total é:',medtt)

