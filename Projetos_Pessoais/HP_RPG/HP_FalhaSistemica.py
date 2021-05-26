entrada1 = int(input('Quantidade de frases a serem manipuladas: '))


def concatenar(frase):
    escopo_frase = frase.strip().upper().split()
    concatenada = ''
    for a in range(len(escopo_frase)):
        concatenada += escopo_frase[a]
    return concatenada


for i in range(entrada1):
    frase = input('Frase: ')
    print(f'{i+1}° Frase-\n')
    frase = concatenar(frase)
