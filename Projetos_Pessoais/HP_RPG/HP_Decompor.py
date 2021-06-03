x = int(input('Quantidade de frases a serem catalogadas: '))
for k in range(x):
    entrada = input('Frase a ser manipulada: ').strip()
    print(f'{k}°->')
    for j in range(len(entrada), 0, -1):
        if entrada[j-1] != ' ':
            print(f'{entrada[0:j]}')
