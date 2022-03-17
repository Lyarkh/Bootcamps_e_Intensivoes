# código referente à aula 05 - Desenvolvendo um ocultador de arquivos
# Nesse código vai usar um arquivo txt chamado 'ocultar.txt' que se encontra na pasta 'Arquivos_txt'
import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('Arquivos_txt/ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado!')
else:
    print('Arquivo não foi ocultado.')