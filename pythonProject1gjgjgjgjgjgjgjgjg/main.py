import os
import pickle
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


def cook_soup(driver):
    return BeautifulSoup(driver.page_source, features='lxml')

def parse_page(soup):
    articles = soup.find_all('article', class_='product_pod')

    data = []

    for article in articles:
        href = article.h3.a['href']
        url = 'https://books.toscrape.com/' + href
        div = article.find('div', class_='product_price')
        price = div.find('p', class_='price_color').text
        in_stock = div.find('p',class_='instock availability').text.strip()
        data.append([url, price, in_stock])
    return data

for i in range(1,51):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    driver.get(url)
    sleep(3)
    soup = cook_soup(driver)
    data = parse_page(soup)
    if os.path.exists('data.pickle'):
        with open('data.pickle', 'rb') as f:
            data_list = pickle.load(f)
        data += data_list


with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)
