# código referente à aula 01 - Introdução á segurança da informação e ping
import os

# Fazendo um código bem simples para verificação do ping entre nós
# Recebendo apenas uma host ou ip
def ping_simples():
    print('=' * 50)
    ip_ou_host = input('Digite o IP ou host a ser verificado: ')
    chamando_o_comando_ping(ip_ou_host)

# Criando função para chamar o comando ping do sistema
def chamando_o_comando_ping(ip_ou_host, pacotes=8):
    print('=' * 50)
    os.system(f'ping -n {pacotes} {ip_ou_host}')
    print('=' * 50)

# Programa para verificar o ping de vários hosts
# os Hosts a serem verificado a conexão esta em 'hosts.txt'
def ping_com_multiplos_hosts():

    # abrindo o txt para pegar os hosts para o comando 'ping'
    with open('Arquivos_txt/hosts.txt', mode='r') as arquivo:
        hosts = arquivo.read()
        hosts = hosts.splitlines()
    
        for host in hosts:
            print(f'Verificando conexão com {host}')
            chamando_o_comando_ping(host, 4)
            

        
if __name__ == '__main__':
    ping_com_multiplos_hosts()