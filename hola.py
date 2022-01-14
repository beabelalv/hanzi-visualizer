import re
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup

def scraping():
    url = 'https://hanpath.com/blog/hsk-3-vocabulary-list/'
    html = urllib.request.urlopen(url)    
    soup = BeautifulSoup(html, 'html.parser')
    tabla = soup.find('table')
    hanzis = tabla.find_all('tr')
    links = []

    for hanzi in hanzis:
        lista = hanzi.find_all('td')
        caracteres = []
        caracteres.clear()
        for elemento in lista:
            caracteres.append(elemento.text)
        links.append(caracteres)
    print(links)

def start():
    scraping()
    
if __name__ == "__main__":
    start()