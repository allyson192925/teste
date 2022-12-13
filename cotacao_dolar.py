from email import header
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import pandas as pd

for i in range(30):
#while True:
    requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    #page = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    tabela = pd.read_excel("Cotações.xlsx")
    tabela.loc[0, "Cotação"] = float(cotacao_dolar)
    tabela.loc[1, "Cotação"] = float(cotacao_euro)
    tabela.loc[2, "Cotação"] = float(cotacao_btc) * 1000
    tabela.loc[0, "Data Última Atualização"] = datetime.now()

    tabela.to_excel("Cotações.xlsx", index=False)
    print(f"Cotação Atualizada.{datetime.now()}")

    time.sleep(60 * 60)
    #soup = BeautifulSoup(page.content, 'html.parser')

    #atributos = {'class': 'g'}
    #respostas = soup.find_all('div', class_='g')
    #respostas = soup.find_all('div', attrs=atributos)
    #print(respostas)




