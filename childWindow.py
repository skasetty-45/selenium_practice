import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
driver.get("https://the-internet.herokuapp.com/windows") # Sample website for Testing windows testing
driver.implicitly_wait(2)
driver.find_element(By.LINK_TEXT,"Click Here").click()

#Get the windows list
windows_open = driver.window_handles
assert len(windows_open) > 1
#swicth to new window
driver.switch_to.window(windows_open[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

#Switch to Parent Window
driver.switch_to.window(windows_open[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
