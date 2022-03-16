# Código referente à aula 02 - Introdução a Socket e cliente TCP/UDP e Server
import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso!')

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = '\nServidor: Olá cliente, tudo sim e com  você?'

while True:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)


# Para ter a conexão do server entre o cliente, rode o arquivo 'server_udp' e depois rode 'cliente_udp' junto
# Assim os dois estarão se conectando