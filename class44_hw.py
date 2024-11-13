from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

try:
    radioButtons = driver.find_elements(By.XPATH,"//input[@type='radio']")
    #print(len(radioButtons)) # to make sure we got the elements
    for radioButton in radioButtons:
        if radioButton.get_attribute("value") == "radio3":
            #print("element Found")
            radioButton.click()
            break

except NoSuchElementException:
    print("Could not find radio buttons on the page.")
except WebDriverException as e:
    print(f"WebDriver error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    driver.save_screenshot("test_result.png")
    driver.quit()