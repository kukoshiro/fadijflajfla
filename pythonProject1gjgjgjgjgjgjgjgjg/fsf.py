import pickle
from bs4 import BeautifulSoup

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html_doc = f.read()
    return BeautifulSoup(html_doc, features='lxml')


soup = read_file('books.html')
articles = soup.find_all('article', class_='product_pod')

data = []

for article in articles:
    href = article.h3.a['href']
    url = 'https://books.toscrape.com/' + href
    div = article.find('div', class_='product_price')
    price = div.find('p', class_='price_color').text
    in_stock = div.find('p',class_='instock availability').text.strip()
    data.append([url, price, in_stock])


with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)
