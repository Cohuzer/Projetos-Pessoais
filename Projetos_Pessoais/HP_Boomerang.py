entrada1 = int(input('Número de frases a serem registradas: '))
for k in range(0, entrada1):
    normal = 0
    reverso = -1
    entrada = str(input('Insira a frase a ser boomerangada: '))
    entrada = entrada.replace(' ', '')
    entrada = entrada.replace('.', '')
    entrada = entrada.upper()

    for i in range(0, len(entrada)):
        print(f'{entrada[normal]}{entrada[reverso]}')
        if normal < len(entrada):
            normal += 1
            reverso -= 1
