from lib2to3.pgen2 import driver
from turtle import title
from selenium import webdriver

import time

driver = webdriver.Edge()

url = "https://www.hatacozumtr.com"
driver.get(url)

url2 = "https://github.com/EyupAtalay"

time.sleep(2)

driver.maximize_window()

print(driver.title)

driver.get(url2)

if "EyupAtalay" in driver.title:
      driver.save_screenshot("seleniumbotdeneme.png")


time.sleep(2)
driver.back()


time.sleep(2)



driver.close()

