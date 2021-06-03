#PROCESSAMENTO
def concatenar(frase):
    escopo_frase = frase.strip().upper().split()
    concatenada = ''
    for a in range(len(escopo_frase)):
        concatenada += escopo_frase[a]

    return concatenada


def fraseFormatada(frase):
    frase_escopo = []
    for i in range(len(frase), 0, -1):
        frase_escopo.append(frase[-i])

    for i in range(1, len(frase)+1):
        frase_escopo.append(frase[-i])

    return ''.join(frase_escopo)



def trocaIndo(quero_trocar, trocar_por, frase):
    nova = []
    x = 0
    for c in frase:
        if c == quero_trocar and x != controle:
            nova.append(trocar_por)
            x += 1
        else:
            nova.append(c)

    return ''.join(nova)


def trocaVoltando(quero_trocar, trocar_por, frase):
    global nova2
    nova = []
    nova2 = []
    x = 0
    for c in range(1, len(frase)+1):
        if frase[-c] == quero_trocar and x != controle:
            nova.append(trocar_por)
            x += 1
        else:
            nova.append(frase[-c])
    for i in range(1, len(nova)+1):
        nova2.append(nova[-i])

    return ''.join(nova2)


def falha(frase):
    global controle
    frase = fraseFormatada(frase)
    retorno = []
    controle = 1
    for a in range(round(len(frase)/2)):
        letra_controle = frase[controle]
        letra_controle_inverso = frase[-controle-1]
        retorno.append(frase)
        frase = trocaIndo(frase[controle-1], letra_controle, frase)
        frase = trocaVoltando(frase[-controle], letra_controle_inverso, frase)
        controle += 1

    tamanho_retorno = len(retorno) - 1
    for i in range(1, len(retorno)):
        tamanho_retorno -= 1
        retorno.append(retorno[tamanho_retorno])

    return retorno


#ENTRADA
frase = input('Frase: ').strip()
frase = concatenar(frase)
falha_respondido = falha(frase)

#SAIDA
print('```')
for z in range(len(falha_respondido)):
    print(falha_respondido[z])
print('```')
