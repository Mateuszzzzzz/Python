import requests
from bs4 import BeautifulSoup

url=("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")

polaczenie = requests.get(url)
polaczenie_html = polaczenie.text

zupa = BeautifulSoup(polaczenie_html, "html.parser")

szukane = zupa.find_all('p')
for element in szukane:
    print(str(element.get_text()))
