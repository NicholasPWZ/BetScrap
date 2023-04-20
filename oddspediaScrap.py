from selenium import webdriver
from bs4 import BeautifulSoup as bs 
import requests


def odds_basketball():
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
        data = bsoup.find('span', class_='event-start-date').text.strip()
        partida = bsoup.find('title').text.strip()
        partida = partida.split('»')
        partida = partida[0] 
        times = partida.split(' x ')
        time1 = times[0]
        time2 = times[-1]
        partida += data
        data_storage[partida] = {}
        eoc_single = bsoup.find('div', class_='eoc-single')
        bookmaker_tag = eoc_single.find_all('div',class_='eoc-table__row__bookmaker')
        bookmaker = [tag.get_text().strip() for tag in bookmaker_tag]
        odds_tag = eoc_single.find_all('span', class_='bookmaker-link cursor-pointer')
        odds = [tag.get_text().strip() for tag in odds_tag]
        odd1maior = 0.0
        odd2maior = 0.0
        odds = odds[2:]
        y = 0
        for p in bookmaker:
            data_storage[partida][p] = {}
            data_storage[partida][p][time1] =  odds[y]
            data_storage[partida][p][time2] =  odds[y+1]
            y+=2
        for p in data_storage[partida]:
            if float(data_storage[partida][p][time1]) > odd1maior:
                odd1maior = float(data_storage[partida][p][time1])
                casa1maior = p
            if float(data_storage[partida][p][time2]) > odd2maior:
                casa2maior = p
                odd2maior = float(data_storage[partida][p][time2])
        
        stake = 100
        def calc_percent(odd1, odd2):
            return (1/odd1 + 1/odd2) * 100
        
        def calc_profit_money(odd1, odd2, stake):
            return (stake / (calc_percent(odd1, odd2) / 100)) - stake
        
        def calc_profit_percent(odd1, odd2):
            return(-100 * (1 - (odd1 * odd2 / (odd1 + odd2))))
        
        def calc_stake(odd1, odd2, stake):
            percernt_odd1 = (1/odd1) * 100
            percernt_odd2 = (1/odd2) * 100
            stake_odd1 = (stake * percernt_odd1) / calc_percent(odd1, odd2)
            stake_odd2 = (stake * percernt_odd2) / calc_percent(odd1, odd2)
            return f'Stake na odd {odd1} X {stake_odd1} = {odd1 * stake_odd1}\nStake na odd {odd2} X {stake_odd2} = {odd2 * stake_odd2}'
        return partida, casa1maior ,odd1maior, casa2maior, odd2maior, '=', calc_profit_percent(odd1maior, odd2maior),'%', calc_stake(odd1maior, odd2maior, stake) 

#def odds_football():
driver = webdriver.Chrome()
driver.get("https://oddspedia.com/br/futebol#odds")
page_source = driver.page_source
driver.quit()

soup = bs(page_source, 'html.parser')
application = soup.find_all(type='application/ld+json')

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
    if 'https://oddspedia.com/br/futebol' not in i:
        continue
    driver = webdriver.Chrome()
    driver.get(i)
    page_html = driver.page_source
    driver.quit()
    bsoup = bs(page_html, 'html.parser')
    try:
        data = bsoup.find('span', class_='event-start-date').text.strip()
    except:
        continue
    partida = bsoup.find('title').text.strip()
    partida = partida.split('»')
    partida = partida[0] 
    times = partida.split(' x ')
    time1 = times[0]
    time2 = times[-1]
    partida += data
    data_storage[partida] = {}
    try:
        eoc_single = bsoup.find('div', class_='eoc-single')
        bookmaker_tag = eoc_single.find_all('div',class_='eoc-table__row__bookmaker')
        bookmaker = [tag.get_text().strip() for tag in bookmaker_tag]
        odds_tag = eoc_single.find_all('span', class_='bookmaker-link cursor-pointer')
        odds = [tag.get_text().strip() for tag in odds_tag]
    except:
        continue
    odd1maior = 0.0
    oddtiemaior = 0.0
    odd2maior = 0.0
    odds = odds[3:]
    y = 0
    for p in bookmaker:
        data_storage[partida][p] = {}
        data_storage[partida][p][time1] =  odds[y]
        data_storage[partida][p]['empate'] =  odds[y+1]
        data_storage[partida][p][time2] =  odds[y+2]
        y+=3
    for p in data_storage[partida]:
        if float(data_storage[partida][p][time1]) > odd1maior:
            odd1maior = float(data_storage[partida][p][time1])
            casa1maior = p
        if float(data_storage[partida][p]['empate']) > oddtiemaior:
            oddtiemaior = float(data_storage[partida][p]['empate'])
            casatiemaior = p
        if float(data_storage[partida][p][time2]) > odd2maior:
            casa2maior = p
            odd2maior = float(data_storage[partida][p][time2])
    stake = 100
    def calc_percent(odd1, oddtie, odd2):
        return (1/odd1 + 1/oddtie + 1/odd2) * 100
    
    def calc_profit_money(odd1, oddtie, odd2, stake):
        return (stake / (calc_percent(odd1, oddtie, odd2) / 100)) - stake
    
    def calc_profit_percent(odd1, oddtie, odd2):
        return(((1 / (calc_percent(odd1, oddtie, odd2) / 100))* 100) / 1) - 100
    
    def calc_stake(odd1, oddtie, odd2, stake):
        percernt_odd1 = (1/odd1) * 100
        percernt_oddtie = (1/oddtie) * 100
        percernt_odd2 = (1/odd2) * 100
        
        stake_odd1 = (stake * percernt_odd1) / calc_percent(odd1,oddtie, odd2)
        stake_oddtie = (stake * percernt_oddtie) / calc_percent(odd1, oddtie, odd2)
        stake_odd2 = (stake * percernt_odd2) / calc_percent(odd1,oddtie, odd2)
        return f'Stake na odd {odd1} X {stake_odd1} = {odd1 * stake_odd1}\nStake na odd {oddtie} X {stake_oddtie} = {oddtie * stake_oddtie}\nStake na odd {odd2} X {stake_odd2} = {odd2 * stake_odd2}'   
    print(partida,'\n', casa1maior ,odd1maior, casatiemaior, oddtiemaior, casa2maior, odd2maior, '=', calc_profit_percent(odd1maior,oddtiemaior, odd2maior),'%\n', calc_stake(odd1maior, oddtiemaior, odd2maior, stake),'\n')    



    