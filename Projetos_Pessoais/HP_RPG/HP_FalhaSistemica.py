entrada1 = int(input('Número de frases a serem registradas: '))


def EscreverFrente(frase):
    for i in range(0, len(frase)):
        print(f'{frase[i]}', end='')


def EscreverContrario(frase):
    for j in range((len(frase) - 1), -1, -1):
        print(f'{frase[j]}', end='')


for k in range(0, entrada1):
    entrada = str(input(f'\n{k + 1}°- Frase: '))
    entrada = entrada.upper()
    entrada = entrada.replace('´', '`')
    entrada = entrada.replace('`', '´')
    entrada = entrada.replace(' ', '')
    copia_entrada = entrada

    for a in range(0, 2 * len(entrada)):
        EscreverFrente(entrada)
        EscreverContrario(entrada)
