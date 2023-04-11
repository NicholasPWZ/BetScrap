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
    
def getodd(url):
    capturar_odd = geturls(url)
    data_storage = {}
    for p in capturar_odd:
        fonte_odd = requests.get(p).text
        soup_odd = bs(fonte_odd, 'html.parser')
        body_classe = soup_odd.find('body')
        script = body_classe.find('script').string
        index_dict = script.find('{')
        script = script[index_dict:]
        dict_odds = json.loads(script)
        nome_partida = dict_odds['data']['event']['shortName']
        data_storage[nome_partida] = { }
        data_storage['url'] = p
        for i in dict_odds['data']['event']['markets']:
            data_storage[nome_partida][i['name']] = {}
            for x in i['selections']:
                data_storage[nome_partida][i['name']][x['name']] = x['price']
                
    return data_storage

