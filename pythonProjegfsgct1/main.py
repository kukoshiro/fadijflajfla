import pickle
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

visited_urls = []

driver = webdriver.Chrome()
url = ('https://www.youtube.com/@algoritmikakz/videos')
driver.get(url)
sleep(5)


meta_info_len = 0
xpath = '//*[@id="page-manager"]/ytd-browse[1]//div[@id="meta"]'
meta_info = driver.find_elements('xpath', xpath)

while meta_info_len != len(meta_info):
    meta_info_len = len(meta_info)
    driver.find_element('xpath', '/html/body').send_keys(Keys.CONTROL + Keys.END)
    sleep(3)
    meta_info = driver.find_elements('xpath', xpath)


lst = []
for info in meta_info:
    lst.append(info.text)


with open('data.pickle', 'wb') as f:
    pickle.dump(lst, f)

