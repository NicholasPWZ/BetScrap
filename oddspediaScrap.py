from selenium import webdriver
from bs4 import BeautifulSoup as bs 
import requests

driver = webdriver.Chrome()
driver.get("https://oddspedia.com/br/basquete/eua/nba")
page_source = driver.page_source
driver.quit()

soup = bs(page_source, 'html.parser')
application = soup.find_all(type='application/ld+json')

# Lista para armazenar os valores das URLs
lista_urls = []

# Loop pelos objetos JSON-LD encontrados
for obj in application:
    # Obtém o valor da chave "url" em cada objeto, se existir
    partes = obj.text.split('"url":"')
    if len(partes) > 1:
        url = partes[1].split('"')[0]
        lista_urls.append(url)

data_storage = {}
lista_urls = list(map(lambda x: x+'#odds', lista_urls))
for i in lista_urls:
    if 'https://oddspedia.com/br/basquete' not in i:
        continue
    driver = webdriver.Chrome()
    driver.get(i)
    page_html = driver.page_source
    driver.quit()
    bsoup = bs(page_html, 'html.parser')
    partida = bsoup.find('div', class_='tip-match__name t-ellipsis').text.strip()
    data_storage[partida] = {}
    eoc_single = bsoup.find('div', class_='eoc-single')
    bookmaker_tag = eoc_single.find_all('div',class_='eoc-table__row__bookmaker')
    bookmaker = [tag.get_text().strip() for tag in bookmaker_tag]
    odds_tag = eoc_single.find_all('span', class_='bookmaker-link cursor-pointer')
    odds = [tag.get_text().strip() for tag in odds_tag]
    odds = odds[2:]
    y = 0
    for p in bookmaker:
        data_storage[partida][p] = {}
        data_storage[partida][p]['odd1'] =  odds[y]
        data_storage[partida][p]['odd2'] =  odds[y+1]
        y+=2
    print(data_storage)
    
    break