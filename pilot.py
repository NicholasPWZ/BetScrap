import requests
import json
from bs4 import BeautifulSoup as bs


def geturls(url):
    fonte = requests.get(url).text
    soup = bs(fonte, 'html.parser')
    type_application = soup.find(type='application/ld+json').string
    url_odd = json.loads(type_application)
    urls = []
    for i in url_odd:
        urls.append(i['url'])
    return urls

capturar_odd = geturls("https://br.betano.com/sport/basquete/ligas/17106r/")

for p in capturar_odd:
    fonte_odd = requests.get(p).text
    soup_odd = bs(fonte_odd, 'html.parser')
    body_classe = soup_odd.find('body')
    script = body_classe.find('script').string
    index_dict = script.find('{')
    script = script[index_dict:]
    dict_odds = json.loads(script)
    dict_section = dict_odds['data']['event']['markets'][0]
    
    for i in dict_odds['data']['event']['markets']:
        print(i['name'])
        for x in i['selections']:
            print(x['name'], x['price'], sep='-->')
    break