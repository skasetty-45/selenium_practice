import time

from selenium import webdriver
from selenium.common import NoSuchElementException, NoSuchFrameException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()

driver.get("https://the-internet.herokuapp.com/iframe") # Sample website for Testing windows testing
driver.implicitly_wait(2)

try:
    driver.find_element(By.XPATH,"//button[contains(@class,'tox-notification__dismiss')]").click()
    driver.switch_to.frame("mce_0_ifr")
    print(driver.find_element(By.ID,"tinymce").text)
    #driver.find_element(By.ID, "tinymce").send_keys("I am able to automate")
    driver.switch_to.default_content() # will switch back to Normal Browser or Frame

except NoSuchFrameException:
    print("Frame error")
finally:
    driver.save_screenshot("test_result.png")
    driver.quit()