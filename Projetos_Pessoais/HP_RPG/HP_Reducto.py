entrada = input('Frase a ser manipulada: ')
entrada = entrada.upper()
print('Frase-')

for j in range(len(entrada), 0, -1):
    if entrada[j-1] != ' ':
        print(f'{entrada[0:j].upper()}{entrada[j:].lower()}')
print(entrada.lower())
