normal = 0
reverso = -1
entrada = str(input('Insira a frase a ser boomerangada: '))
entrada = entrada.upper()

for i in range len(entrada):
    print(f'{entrada[normal]}{entrada[reverso]}')
    if normal < len(entrada):
        normal += 1
        reverso -= 1