lista = []
entrada = input('Frase a ser manipulada: ')
entrada = entrada.upper()
print('Frase-')

print(entrada)
for i in range(len(entrada)):
    print(f'{entrada[0:-i]}{entrada[-i:-1].lower()}')
