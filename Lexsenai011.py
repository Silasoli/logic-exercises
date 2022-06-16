cdali=int(input('Digite o código do alimento:'))
if cdali==1:
    print('Alimento não perecível')
if cdali>=2 and cdali<=4:
    print('Alimento perecível')
if  cdali>=5 and cdali<=6:
    print('Vestuário')
if cdali>=8 and cdali<=15:
    print('Limpeza e utensílios domésticos')
if cdali<1 or cdali>15:
    print('Inválido')
