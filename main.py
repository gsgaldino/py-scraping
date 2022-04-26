from bs4 import BeautifulSoup
import requests

def get_price(founded_price):
  if founded_price is None:
    return 'null'
  return founded_price.text.strip()

def format_spot(spot):
  name = spot.find('h3', class_='spotTitle')
  founded_price = spot.find('span', class_='fbits-spot-boleto-valor')
  price = get_price(founded_price)
  print('name=' + name.text.strip() + ' price=' + price)

url = 'https://madeinbrazil.com.br'

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')
spots = soup.find_all('div', class_='spot')

for spot in spots:
  format_spot(spot)
