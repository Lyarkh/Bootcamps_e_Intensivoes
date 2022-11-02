# código referente à aula 04 - Desenvolvendo gerador de hashs
import hashlib

string = input('Digite o texto a ser gerado a hash: ')
menu = int(input("""
#### Escolha o tipo de hash #### 
[1] MD5
[2] SHA1
[3] SHA256
[4] SHA512
--------------------------------
Digite o número referente ao hash escolhido: """))

tipos_de_hash = [
    [hashlib.md5, 'md5'],[hashlib.sha1, 'sha1'], 
    [hashlib.sha256, 'sha256'],[hashlib.sha512, 'sha512']]

for posicao, _ in enumerate(tipos_de_hash):
    
    if (menu-1) == posicao:
        tipo_hash, nome_hash = tipos_de_hash[posicao]
        resultado = tipo_hash(string.encode('utf-8'))
        print(f'O hash {nome_hash} da string: {string} é:\n{resultado.hexdigest()}')