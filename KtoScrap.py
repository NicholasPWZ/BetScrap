import json
import requests
from bs4 import BeautifulSoup as bs

url = "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=180&langId=79&skinName=kto.com&configId=12&culture=pt-BR&countryCode=BR&deviceType=Desktop&numformat=en&integration=kto.com&sportids=67&categoryids=0&champids=2980&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&startDate=2023-04-11T18%3A07%3A00.000Z&endDate=2023-04-18T18%3A07%3A00.000Z"
fonte = requests.get(url).json()
data = fonte['Result']['Items'][0]


data_storage = {}
for i in data['Events']:
    nome_partida = i['Name']
    if 'vs.' in  i['Name']:
        nome_partida = nome_partida.replace('vs.', '-')
    data_storage[nome_partida] = {}
    data_storage[nome_partida]['name'] = i['Items'][0]['Name']
    data_storage[nome_partida]['equipe'] = i['Items'][0]['Items'][0]
print(data_storage)
