from betanoScrap import getodd
from KtoScrap import getoddKto
import copy

# dados_betano = copy.deepcopy(getodd('https://br.betano.com/sport/basquete/eua/nba/17106/'))
# dados_kto = copy.deepcopy(getoddKto('https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents?timezoneOffset=180&langId=79&skinName=kto.com&configId=12&culture=pt-BR&countryCode=BR&deviceType=Desktop&numformat=en&integration=kto.com&sportids=67&categoryids=0&champids=2980&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&marketGroupId=0&startDate=2023-04-11T18%3A07%3A00.000Z&endDate=2023-04-18T18%3A07%3A00.000Z'))
# print(dados_betano['Toronto Raptors - Chicago Bulls']['Vencedor'].values(), dados_kto['Toronto Raptors - Chicago Bulls']['Vencedor'].values(), sep='\n')

odd1 = 3.2
odd2 = 2.00
calculo = (1/odd1 + 1/odd2) * 100
print(calculo)