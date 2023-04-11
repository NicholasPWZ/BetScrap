from betanoScrap import getodd
import copy

dados_betano = copy.deepcopy(getodd('https://br.betano.com/sport/basquete/eua/nba/17106/'))

print(dados_betano['Miami Heat - Atlanta Hawks']['Vencedor SO'])

odd1 = 1
odd2 = 3
calculo = (1/odd1 + 1/odd2) / 100