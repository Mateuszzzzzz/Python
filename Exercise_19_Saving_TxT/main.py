import requests
from bs4 import BeautifulSoup


url = 'http://nytimes.com'
polacz = requests.get(url)
polacz_html = polacz.text
soup = BeautifulSoup(polacz_html)
for i in soup.find_all('div', class_='css-debyuq e1voiwgp1'):
    written = i.text
    with open('Wrote_file.txt', 'w') as zapisz:
        zapisz.write('written')
        f = open('Wrote_file.txt', 'r')
        f.read()
