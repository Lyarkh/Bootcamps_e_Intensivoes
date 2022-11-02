# Código referente à aula 02 - Introdução a Socket e cliente TCP/UDP e Server
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso!')

host = 'localhost'
porta = 5433
mensagem ='Olá servidor, tudo bem?'

try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    print('Cliente: Fechando a conexão')
    s.close()


# Para ter a conexão do server entre o cliente, rode o arquivo 'server_udp' e depois rode 'cliente_udp' junto
# Assim os dois estarão se conectando