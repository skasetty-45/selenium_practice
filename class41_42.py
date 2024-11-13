# This class is to handle the Auto suggest / Dynamic dropdowns

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.ChromiumEdge()

#Get the URL
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
try:
    driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("Ind")
    time.sleep(3) # Give time for Dropdown to load
    countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
    for country in countries:
        if country.text == "India":
            country.click()
            break #To make sure the needed country is found and we can stop this loop
    #Retrieve the added text in a dynami dropdown
    assert (driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute("value")) == "India"
    driver.save_screenshot("test_passed.png")

except Exception as e:
    driver.save_screenshot("test_failure.png")
    print(e)

finally:
    driver.quit()
