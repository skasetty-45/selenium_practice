import time
from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# 2 Assignments : 1. Make sure the final  amount after discount is less than actual
#2. Prepare a list of items that are seen for each search result


# Click on search and send keys ber
try:
    driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
    time.sleep(3)
    products = driver.find_elements(By.XPATH,"//div[@class='product']/h4")
    assert len(products) > 0
    for product in products:
        print(product.text)
    #Adding the vegetables to cart
    results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
    assert len(results) > 0
    for result in results:
        result.find_element(By.XPATH,"div/button").click()
    # Open cart and Proceed to checkout
    driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
    checkout = driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")
    assert checkout.is_enabled()
    checkout.click()
    #time.sleep(3) # To Make sure the checkout page is loaded
    # Enter Promo code
    driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
    time.sleep(5) # To validate and check the promo code
    promo_status = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
    assert "applied" in promo_status
    assert "10" in driver.find_element(By.CSS_SELECTOR,".discountPerc").text
    assert float(driver.find_element(By.CLASS_NAME,"discountAmt").text) < int(driver.find_element(By.CLASS_NAME,"totAmt").text)


except NoSuchElementException:
    print("Element Not found")
except WebDriverException as e:
    print(f"WebDriver error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    driver.save_screenshot("test_result.png")
    driver.quit()
