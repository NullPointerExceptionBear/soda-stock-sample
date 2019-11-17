from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

print("Hello There")#Friendly

#webdriver location
driver = webdriver.Chrome(executable_path='C:/Programing Stuff/Test/chromedriver_win32/chromedriver.exe')
#Tell automation to wait so some websites don't identify as bot
driver.implicitly_wait(3)
driver.get('https://google.com')
#List of beverages I want to check
sodas = ['Pepsi', 'Coca-Cola', 'Cott', 'Monster Beverage']
for x in sodas:
    print('-------------------')
    print(x)
    driver.find_element_by_name("q").send_keys(x)
    time.sleep(3)
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    try:
        for thing in soup.select('.Z1hOCe'):
            print(thing.text)
    except:
        print("Couldn't do the thing.")
    print('-------------------')
    time.sleep(1)
    driver.get('https://google.com')
driver.quit()