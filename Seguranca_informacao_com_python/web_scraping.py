# código referente à aula 04 - Desenvolvendo Web scraping
from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content

soup = BeautifulSoup(site, 'html.parser')

# print(soup.prettify) mostrando o html da pagina toda

temperatura = soup.find('span', class_='-text -bold -gray-dark-2 -font-55 _margin-l-15') # buscando uma classe ou id especifico

print(temperatura.string)
print(soup.span)
