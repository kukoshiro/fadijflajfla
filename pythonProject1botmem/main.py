import pickle
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver


data = [['про Вовочку', 'https://vse-shutochki.ru/anekdoty-pro/vovochka'],
        ['Про Чебурашку', 'https://vse-shutochki.ru/anekdoty-pro/чебурашка'],
        ['Про медведя', 'https://vse-shutochki.ru/anekdoty-pro/medved']
        ]

def parse_page(soup):
     aneks_list = []
     posts = soup.find_all('div', class_='post noSidePadding')
     for post in posts[:-2]:
         if post.div:
            aneks_list.append(post.div.text.strip())
         return aneks_list

def cook_soup(driver):
    return BeautifulSoup(driver.page_source, features='lxml')


driver = webdriver.Chrome()
aneks = {}
for category, url in data:
    driver.get(url)
    sleep(3)
    soup = cook_soup(driver)
    aneks[category] = parse_page(soup)

with open('aneks.pickle', 'wb') as f:
    pickle.dump(aneks, f)
