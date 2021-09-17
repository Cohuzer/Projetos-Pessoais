from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib
import urllib.request

#Definição das funções
def construtorMensagem(turner, mensagem):
    if turner == "0":
        retorno = str(input(mensagem))
    return retorno


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


def inicializadorWebdriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        site = urllib.request.urlopen('https://web.whatsapp.com/')
    except urllib.error.URLError:
        print('\033[31mWHATSAPP INDISPONIVEL\033[m')
    else:
        driver.get('https://web.whatsapp.com/')
        time.sleep(20)


def buscarContato(contato):
        campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
        #Ambos os Xpath's servem para encontrar as caixas de busca e mensagem do whatsapp
        time.sleep(3)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)


def enviarMensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    #campo_mensagem[0] == Buscar contatos; campo_mensagem[1] == escrever a mensagem
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)


def enviarFigurinha():
    pass

#Código Principal
print('='*60)
print(' '*20, 'WHATSAPP BOT 2')
print('='*60)
print('\n ~> By: Mateus CohuzEr')

# Entrada
turner = lerZeroUm("\nDigite para:\n0-Mensagem de Texto\n1-Figurinha\n>> ") # 1-Manda a figurinha em primeiro lugar nas enviadas recentemente
mensagem = construtorMensagem("0", "Insira a mensagem desejada: ")
contatos = lerList("Insira o nome exato do contato ou grupo desejado")
quantidade_mensagens = int(input("Insira quantas mensagens serão enviadas: "))

#Processamento
inicializadorWebdriver()

if turner == "0":
    for contato in contatos:
        buscarContato(contato)
        for i in range(quantidade_mensagens):
            enviarMensagem(mensagem)
