entrada = input('Frase a ser manipulada: ')
entrada = entrada.upper()
print('Frase-')

print(entrada)
for i in range(len(entrada)):
    for j in range(len(entrada), 0, -1):
        print(f'{entrada[0:j].upper()}{entrada[j:].lower()}')
