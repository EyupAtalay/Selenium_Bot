from lib2to3.pgen2 import driver
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

url = "https://github.com/"
driver.get(url)

searchinput = driver.find_element_by_name("q")

time.sleep(2)
searchinput.send_keys("Windows")
time.sleep(2)
searchinput.send_keys(Keys.ENTER)

result = driver.find_elements_by_css_selector(".repo-list-item a")
time.sleep(4)

for element in  result:
    print(element.text)

driver.close()