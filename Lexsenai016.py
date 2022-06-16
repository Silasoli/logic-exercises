while True:
  if num == 0:
    break
num=int(input('Digite um número:'))
divi2=2
divi3=3
divi5=5
divi7=7
divi11=11
if  num==2 or num==3 or num==5 or num==7 or num==11:
  print('É primo')
elif num == 1:
  print('Não é primo')
elif num%divi2==0 or num%divi3==0 or num%divi5==0  or num%divi7==0  or num%divi11==0:
  print( 'Não é primo')
else:
  print('É primo')
