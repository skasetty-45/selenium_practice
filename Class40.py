# This covers static dropdowns and its selection using selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.ChromiumEdge()

#Get the URL
driver.get("https://rahulshettyacademy.com/angularpractice/")

try:
    driver.find_element(By.NAME,"name").send_keys("Sarat Kasetty")
    driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
    driver.find_element(By.ID,"exampleInputPassword1").send_keys("Hello@1234")
    # Now selecting an Option form static dropdowns
    Select(driver.find_element(By.ID,"exampleFormControlSelect1")).select_by_visible_text("Female")
    driver.save_screenshot("test_passed.png")

except:
    driver.save_screenshot("error.png")
    print("The test failed")

finally:
    driver.quit()