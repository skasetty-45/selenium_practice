from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#The Task is to select a checkbox dynamically positioned which dont have an ID or Name
# 1. Take the list of all checkboxes available in the webpage using findelements
# 2. As the checkbox dont have an ID/Name but has a value , We cba match it through the attribute value and then we can click it
try:
    checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    #print(len(checkboxes)) # to make sure we got the elements
    for checkbox in checkboxes:
        if checkbox.get_attribute("value") == "option2":
            checkbox.click()
            assert checkbox.is_selected()
            break
except Exception as e:
    print("Script has failed")
    print(e)

finally:
    driver.save_screenshot("test_result.png")
    driver.quit()