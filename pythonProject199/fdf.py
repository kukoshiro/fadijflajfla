from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://learn.algoritmika.org/login')
username_input = driver.find_element("xpath",//input[@class="username"])
//*[@id="root"]/div[1]/div/div[2]/form/div[2]/div/input
sleep(3)


