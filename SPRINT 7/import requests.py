import requests
from bs4 import BeautifulSoup
import pandas as pd

# definir a url
url = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'

atributo_id = {"id": "weather_records"}

# função para converter lista em minúscula


def convert_lower(data):
    list_lower = []
    for element in data:
        list_lower.append(element.lower())
    return list_lower

# função para converter para o formato snake_case


def snake_case(data):
    data_snake_case = []
    for element in data:
        data_snake_case.append(element.replace(" ", "_"))
    return data_snake_case

# função para capturar tabela


def heading_scrapping(site, atributo):
    content = []
    req = requests.get(url)  # realizar a solicitação através do protocolo html
    # fazer acesso através do BeatifulSoup
    soup = BeautifulSoup(req.text, 'html.parser')
    table = soup.find('table', attrs=atributo)  # buscar a tabela
    heading_table = []
    for row in table.find_all('th'):  # buscando o cabeçalho th(table header)
        heading_table.append(row.text)
    # heading_lower = convert_lower(heading_table) # convertendo para minúsculo
    # heading_snake_case = snake_case(heading_lower)
    for row in table.find_all('tr'):  # bsucando os valores das linhas
        # não considerango a liha th (cabeçalho, pois já foi acessada)
        if not row.find_all('th'):
            # acessando os valores de cada célula
            content.append([element.text for element in row.find_all('td')])

    # retornado um tupla com cabeçalho, a tabela completa com tags e os valores da tabela
    return heading_table, table, content

# função para converter em dataframe


def convert_to_df(value_content, heading_content):
    df = pd.DataFrame(value_content, columns=heading_content)
    return df


all_table = heading_scrapping(url, atributo_id)  # salvando a tabela
heading_table = all_table[0]  # acessando o cabeçalho
table = all_table[1]  # tabela com tags
values = all_table[2]  # somente os valores de cada linha

weather_records = convert_to_df(values, heading_table)

print(weather_records)
