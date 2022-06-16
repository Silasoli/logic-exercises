num = int(input('Digite o número para achar seus multiplos:'))
aini = int(input('Digite o começo do intervalo:'))
bfin = int(input('Digite o final do intervalo:'))

for x in range(aini, bfin):
    if x % num == 0:
        print('É multiplo', x)
