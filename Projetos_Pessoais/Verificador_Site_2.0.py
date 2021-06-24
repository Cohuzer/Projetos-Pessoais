from subprocess import check_output
from time import sleep

# Verifica a cada 10 segundos se o site em questão está disponível ou não

print('\033[1;35m VERIFICADOR DE ATIVIDADE 2.0\033[m')
print('   >>Digite \033[1:31m\exit\033[m para sair \n')

target = input('\033[34mTarget site: \033[m')  # Link do site

while True:
    try:
        check_output(f"ping {target}", shell=True)
    except:
        print('\033[31mSITE INDISPONIVEL\033[m')
        sleep(5)
    else:
        print(f'\033[32mSITE DISPONIVEL\033[m')
        break

print('\033[1:34m --> Fim da execução do programa\033[m')
