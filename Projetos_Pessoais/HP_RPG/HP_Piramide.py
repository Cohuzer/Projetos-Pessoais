#Piramide

def f1(entrada):
    for i in range(0, len(entrada)):
        try:
            if entrada[i + 1] != ' ':
                print(f'{entrada[0:i + 1]}')
        except IndexError:
                print(f'{entrada}')

def f2(entrada):
    for c in range(0, len(entrada)):
        try:
            if entrada[-(c + 1)] != ' ':
                print(f'{entrada[0:-(c + 1)]}')
        except IndexError:
            print(f'{entrada[0]}')

for posi in range(1):
    print(f'\033[1;33mPiramide {posi + 1}:\033[m')

    entrada = str(input('Frase: ')).strip()
    f1(entrada)
    f2(entrada)

    #Piramide Inversa
    print(f'\033[1;33mPiramide Inversa {posi + 1}:\033[m')

    print(f'{entrada}')
    f2(entrada)
    f1(entrada)
