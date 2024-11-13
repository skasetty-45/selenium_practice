import time
from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Click on search and send keys ber
try:
    driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
    time.sleep(3)
    results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
    assert len(results) > 0
    #Adding the vegetables to cart
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

    # check the totals
    prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
    total_price = 0
    for price in prices:
        total_price = total_price + int(price.text)
    #print(total_price)
    assert total_price == float(driver.find_element(By.CLASS_NAME,"totAmt").text)
except NoSuchElementException:
    print("Element Not found")
except WebDriverException as e:
    print(f"WebDriver error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    driver.save_screenshot("test_result.png")
    driver.quit()
