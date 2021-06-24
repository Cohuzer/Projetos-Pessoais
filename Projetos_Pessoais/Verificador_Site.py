import urllib.error
import urllib.request
from time import sleep

# Verifica a cada 10 segundos se o site em questão está disponivel ou não

print('\033[1;35m VERIFICADOR DE ATIVIDADE 1.0\033[m')
print('   >>Digite \033[1:31m\exit\033[m para sair \n')

entrada = input('\033[34mTarget site: \033[m') #Link do site

while True:
    try:
        site = urllib.request.urlopen(entrada)
    except urllib.error.URLError or urllib.error.HTTPError:
        print('\033[31mSITE INDISPONIVEL\033[m')
        sleep(10)
    else:
        print(f'\033[32mSITE DISPONIVEL\033[m')
        break

print('\033[1:31mFim da execução do programa\033[m')
