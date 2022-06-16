def maior(lista):
  maxi=max(lista)
  return maxi



def ordena(num1,num2,num3):
  lis1=[]
  lis1.append(num1)
  lis1.append(num2)
  lis1.append(num3)
  menor=min(lis1)
  lis1.remove(menor)
  maior=max(lis1)
  lis1.remove(maior)
  meio=max(lis1)
  lisordem=[]
  lisordem.append(menor)
  lisordem.append(meio)
  lisordem.append(maior)
  return lisordem



def ocorrencia(lista,num):
  lioc=[]
  for i in lista:
    if i==num:
      lioc.append(num)
  return (len(lioc))



def limite(num,liminf,limitsup):
  if limitsup>num>liminf:
    return True
  return False



def categoria(num):
  if num>=5 and num<=7:
    return 'Infantil A'
  if num>=8 and num<=10:
    return 'Infantil B'
  if num>=11 and num<=13:
    return 'Juvenil A'
  if num>=14 and num<=17:
    return 'Juvenil B'
  if num>=18:
    return 'Adulto'


def lista_nomes():
  name=input('Digite um nome:')
  lisname=[]
  while name!='0':
    if name=='0':
      break
    else:  
      lisname.append(name)
      name=input('Digite um nome:')
  return lisname