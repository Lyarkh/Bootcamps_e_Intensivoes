# código referente à aula 05 - Desenvolvendo um verificador de IP Externo
import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print(f"""
============================
   Detalhes do IP externo 
IP: {ip}
Organização: {org}
Cidade: {cidade}
Pais: {pais}
Região: {regiao}
============================

""")

# Os dados mostrados nesse códigos são suas informações de IP reais, cuidado ao divulgar.