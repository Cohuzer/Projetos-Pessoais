x = int(input('Quantidade de frases a serem catalogadas: '))
for i in range(x):
    entrada = input('Frase a ser manipulada: ').strip()
    entrada = entrada.upper()
    print(f'{i+1}° Frase-')

    for j in range(len(entrada), 0, -1):
        if entrada[j-1] != ' ':
            print(f'{entrada[0:j].upper()}{entrada[j:].lower()}')
    print(entrada.lower())
