# Código referente à aula 03 - Desenvolvimento de ferramentas parte 1 - Trabalhando com Threads e IP's
import ipaddress

ip1 = '192.168.0.1'
ip2 = '192.168.0.0/0'

endereço = ipaddress.ip_address(ip1)
rede = ipaddress.ip_network(ip2, strict=False)

print(endereço + 267)

for i in rede:
    print(i)