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


lista_urls = list(map(lambda x: x+'#odds', lista_urls))
for i in lista_urls:
    if 'https://oddspedia.com/br/basquete' not in i:
        continue
    driver = webdriver.Chrome()
    driver.get(i)
    page_html = driver.page_source
    driver.quit()
    bsoup = bs(page_html, 'html.parser')
    eoc_single = bsoup.find('div', class_='eoc-single')
    print(eoc_single.find('span',class_='eoc-max-odds__odd__val'))
    
    break