from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib
import urllib.request

print('='*60)
print('WHATSAPP BOT')
print('='*60)
print('\n By: Mateus CohuzEr')


contatos = []
#Declaração de variavel, evita mudar essa parte

quantidade_contatos = int(input('Quantos contatos receberão as mensagens? '))
for i in range(quantidade_contatos):
    contatos.append(str(input('Insira o nome exato do(s) contato(s): ')))

mensagem = str(input('Insira a mensagem: '))
quantidade_mensagens = int(input('Vezes que essa mensagem sera enviada: '))

driver = webdriver.Chrome(ChromeDriverManager().install())

#Whatsapp Check e executação do código
try:
    site = urllib.request.urlopen('https://web.whatsapp.com/')
except urllib.error.URLError:
    print('\033[31mWHATSAPP INDISPONIVEL\033[m')
else:
    driver.get('https://web.whatsapp.com/')
    time.sleep(15)
    #Se quiser aumentar/diminuir esse tempo, vai do seu processamento
    def buscar_contato(contato):
        campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
        #Ambos os Xpath's servem para encontrar as caixas de busca e mensagem do whatsapp
        time.sleep(3)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)

    def enviar_mensagem(mensagem):
        campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
        #Pelo dois Xpath's terem o mesmo titulo você os coloca numa lista e busca o desejado, no primeiro caso queremos o primeiro campo que aparece na busca, porém nesse queremos o segundo
        # campo_mensagem[0] == Buscar contatos ; campo_mensagem[1] == escrever a mensagem
        campo_mensagem[1].click()
        time.sleep(1)
        campo_mensagem[1].send_keys(mensagem)
        campo_mensagem[1].send_keys(Keys.ENTER)

    for contato in contatos:
        buscar_contato(contato)
        for i in range(0, quantidade_mensagens):
            enviar_mensagem(mensagem)
