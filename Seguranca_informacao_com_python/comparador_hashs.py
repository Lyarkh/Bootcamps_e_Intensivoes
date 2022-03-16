# Código referente à aula 03 - Desenvolvimento de ferramentas parte 1 - Comparador de Hashs
import hashlib

# Nesse código vai usar arquivos txt que estarão na pasta 'Arquivo_txt'
# Serão usados os arquivos "hash_a.txt" e "hash_b.txt"

arquivo_01 = 'Arquivos_txt/hash_a.txt'
arquivo_02 = 'Arquivos_txt/hash_b.txt'

hash_01 = hashlib.new('ripemd160')
hash_02 = hashlib.new('ripemd160')

hash_01.update(open(arquivo_01, 'rb').read())
hash_02.update(open(arquivo_02, 'rb').read())

if hash_01.digest() != hash_02.digest():
    print(f'O arquivo: ({arquivo_01}) é diferente do arquivo: ({arquivo_02})')
    print('-'* 50)
    print(f'O hash do arquivo hash_01.txt é {hash_01.hexdigest()}')
    print(f'O hash do arquivo hash_02.txt é {hash_02.hexdigest()}')
    print('-'* 50)

else:
    print(f'O arquivo: ({arquivo_01}) é igual do arquivo: ({arquivo_02})')
    print('-'* 50)
    print(f'O hash do arquivo hash_01.txt é {hash_01.hexdigest()}')
    print(f'O hash do arquivo hash_02.txt é {hash_02.hexdigest()}')
    print('-'* 50)