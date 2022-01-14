from main.models import Anime, Genre, Rating
import urllib.request
import re

def deleteTables():
    Hanzi.objects.all().delete()


def populateHanzis():
    Hanzi.objects.all().delete()
    print("Loading Hanzis...")
       
    lista = []
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

def main():
    populateHanzis()
    print("Finished database population")

main()