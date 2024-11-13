import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
time.sleep(5)
#get a URL
driver.get("https://rahulshettyacademy.com/client")

try:
    driver.find_element(By.LINK_TEXT,"Forgot password?").click()
    new_page = driver.current_url
    assert "password-new" in new_page
    driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
    driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    driver.save_screenshot("hello.png")

except:
    driver.get_screenshot_as_png()
    print("The run has encountered an Error")

finally:
    driver.quit()
