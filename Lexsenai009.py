la1=float(input('Digite o tamanho do primeiro lado:'))
la2=float(input('Digite o tamanho do segundo lado:'))
la3=float(input('Digite o tamanho do terceiro lado:'))
if la1==la2==la3:
    print('Equilátero')
elif la1!=la2 and la1!=la3 and la2!=la3:
    print('Escaleno')
else:
    print('Isósceles')
