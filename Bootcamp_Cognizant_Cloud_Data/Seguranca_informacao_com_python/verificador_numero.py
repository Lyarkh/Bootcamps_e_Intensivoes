# código referente à aula 05 - Desenvolvendo um verificador de numero de telefone
import phonenumbers
from phonenumbers import geocoder

telefone = input('Digite o telefone no formato: +551140028922: ')

phone_number = phonenumbers.parse(telefone)
cidade_telefone = geocoder.description_for_number(phone_number, 'pt')

print(cidade_telefone)
