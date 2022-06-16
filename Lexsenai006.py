sexo=int(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino:'))
alt=float(input('Altura:'))

peso_ideal=(72.7*alt-58) if sexo == 1 else (62*alt-44.7)
print('Seu peso ideal é:',peso_ideal)
