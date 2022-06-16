nume=[]
num=int(input('Digite um número:'))
while num!=0:
  nume.append(num)
  num=int(input('Digite um número:'))
  nume.append(num)
maxi=max(nume)
print('O maior número digitado foi:',maxi)
nume.pop()
mini=min(nume)
print('O menor número digitado foi:', mini)




