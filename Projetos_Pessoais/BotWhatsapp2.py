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
        escopo = str(input("\n" + mensagem + ": "))
        lista.append(escopo)
        c += 1
        escopo_boll = str(input("Digite 0 se já inseriu todos os contatos desejados: "))
        if escopo_boll == "0":
            break
    return lista


def lerZeroUm(mensagem):
    retorno = str
    while (True):
        retorno = str(input(mensagem))
        if retorno in "01":
            break
    return retorno


print('='*60)
print(' '*20, 'WHATSAPP BOT 2')
print('='*60)
print('\n ~> By: Mateus CohuzEr')

mensagem = str
turner_sticker = lerZeroUm("\nDigite para:\n0-Mensagem de Texto\n1-Figurinha\n>> ")
contatos = lerList("Insira o nome exato do contato ou grupo desejado")
quantidade_mensagens = int(len(contatos))