import requests
from time import sleep
from bs4 import BeautifulSoup

res = requests.get('http://lib.ru/POEZIQ/')
soup = BeautifulSoup(res.text, features='lxml')
elements = soup.find_all(['dir', 'li'])
genre = ''
lst = []

for element in elements:
    if element.name == 'dir':
        genre = element.text
    if element.name == 'li':
        a = element.find('a')
        text = element.text.replace('\xa0', '').strip()
        text = " ".join(text.split()[-2:])
        if 'http' not in a['href']:
            href = 'http://lib.ru/POEZIQ' + a['href']
        else:
            href = a['href']
        data = [genre, text, href]
        if 'поэзия' in genre:
            lst.append(data)
            print(data)