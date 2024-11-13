# This test is to test the Alert popups

from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

try:
    driver.find_element(By.XPATH,"//input[@name='enter-name']").send_keys("Sarat")
    assert driver.find_element(By.XPATH,"//input[@name='enter-name']").get_attribute("value") == "Sarat"
    driver.find_element(By.ID,"alertbtn").click()
    alert = driver.switch_to.alert
    alert.accept()

except NoSuchElementException:
    print("text box Not found")
except WebDriverException as e:
    print(f"WebDriver error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    driver.save_screenshot("test_result.png")
    driver.quit()