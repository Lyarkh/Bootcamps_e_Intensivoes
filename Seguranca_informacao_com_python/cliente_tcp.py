# Código referente à aula 02 - Introdução a Socket e cliente TCP/UDP e Server
import socket
import sys

# Criando uma conexão de cliente pelo protocolo TCP 
def main():
    # Criando a conexão socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!')
        print(f'Erro: {e}')
        sys.exit()
    
    host_alvo = input('Digite o host ou IP a ser conectado: ')
    porta_alvo = input('Digite a porta a ser conectada: ')

    print('Socket criado com sucesso!')

    # Testando uma conexão de host + porta adicionada pelo usuário
    try:
        s.connect((host_alvo, int(porta_alvo)))
        print(f'Cliente TCP conectado com sucesso no host: {host_alvo} pela porta: {porta_alvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f'Não foi possível conectar no host: {host_alvo} pela porta: {porta_alvo}')
        print(f'Erro: {e}')
        sys.exit()
      
if __name__ == '__main__':
    main()