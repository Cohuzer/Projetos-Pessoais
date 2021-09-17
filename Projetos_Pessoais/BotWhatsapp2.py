from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib
import urllib.request


def lerList(mensagem):
    lista = []
    c = 0
    while (True):
        escopo = str(input(mensagem + ": "))
        lista.append(escopo)
        c += 1
        escopo_boll = str(input("Digite 0 para encerrar o programa: "))
        if escopo_boll == "0":
            break
    return lista


def lerZeroUm(mensagem):
    retorno = str
    while (True):
        try:
            retorno = str(input(mensagem))
            if retorno in "01":
                break
        except (ValueError):
            print('\033[31mVALOR INVALIDO! Digite um valor valido\033[m')
        except(TypeError):
            print(f'\033[31mVALOR INVALIDO! Informe um número valido!\033[m')
        except(KeyboardInterrupt):
            print(f'O usuário preferiu não informar esse número!')
    return retorno


print('='*60)
print(' '*20, 'WHATSAPP BOT 2')
print('='*60)
print('\n By: Mateus CohuzEr \n')

mensagem = str
turner_sticker = lerZeroUm("Digite:\n0-Mensagem de Texto\n1-Figurinha\n>>")
quantidade_mensagens = int
contatos = lerList("Insira o nome exato do contato ou grupo desejado")

