import time

from selenium import webdriver

driver = webdriver.ChromiumEdge()
driver.get("https://www.gmail.com")
time.sleep(5)
