c = 0
quantiaFrases = int(input('Quantidade de frases serão catalogadas: '))
quantiaFrases = quantiaFrases
while c != quantiaFrases:
    entrada = str(input('\nFrase do acróstico: '))
    multiplicacao = int(input('Valor para multiplicar: '))
    x = 0
    print(f'{c + 1}.', end=' ')
    for i in range(0, len(entrada)):
        print(f'{entrada[x]}'*multiplicacao, end='')
        x = x + 1
    c += 1
