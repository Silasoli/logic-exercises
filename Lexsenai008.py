sal1=int(input('Digite o primeiro salário:'))
sal2=int(input('Digite o segundo salário:'))
sal3=int(input('Digite o terceiro salário:'))
if sal1>sal2 and sal3:
    print ("O maior salário é:", sal1)
if sal2>sal1 and sal2>sal3:
   print("O maior salário é:", sal2)
if sal3>sal1 and sal2:
   print("O maior salário é:", sal3)
