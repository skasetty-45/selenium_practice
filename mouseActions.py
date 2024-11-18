import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# This class is to check the functions of actions Keyword
# step1 - creation of an Action object
# context click = Right click
# click and hold = Long press
# Drag and Drop
# To perform any actions listed above we should call .perform() method at the end of the line
try:
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
    driver.find_element(By.LINK_TEXT,"Reload").click()
    time.sleep(3) # To see the reload of window

except NoSuchElementException:
    print("Element not found")

finally:
    driver.save_screenshot("test_result.png")
    driver.quit()
