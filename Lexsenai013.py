print('Formas de pagamento')
print('1- À vista em dinheiro ou débito, recebe 10% de desconto')
print('2- À vista no cartão de crédito, recebe 5% de desconto')
print('3- Em duas vezes, preço normal na etiqueta sem juros')
print('4- Em três vezes, preço normal de etiqueta e juros de 10%')
fdp=int(input('Digite o número da forma de pagamento:1,2,3 ou 4:'))
valdop=float(input('Digite o valor do produto:'))
if fdp==1:
  valcmd=float((valdop-(valdop/100*10)))
  print('O valor total de pagamento é', valcmd)
if fdp==2:
  valcmd=float((valdop-(valdop/100*5)))
  print('O valor total de pagamento no cartão é', valcmd)
if fdp==3:
  valcmd=float((valdop/2))
  print('Duas parcelas de', valcmd)
if fdp==4:
  valcmd=float((valdop+(valdop*0.1)))
  vald3=(valcmd/3)
  print('Três parcelas de',vald3)

