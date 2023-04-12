import json
import requests
from bs4 import BeautifulSoup as bs



def getoddKto(url):
    fonte = requests.get(url).json()
    data = fonte['Result']['Items'][0]
    data_storage = {}
    for i in data['Events']:
        nome_partida = i['Name']
        if 'vs.' in  i['Name']:
            nome_partida = nome_partida.replace('vs.', '-')
        data_storage[nome_partida] = {}
        for x in i['Items']:
            selecao = x['Name']
            selecao = selecao.replace('(incluindo Prorrogação)', '').strip()
            data_storage[nome_partida][selecao] = {}
            for p in x['Items']:
                data_storage[nome_partida][selecao][p['Name']] = p['Price']
    return data_storage
