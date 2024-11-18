import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opts = Options()
opts.add_argument("headless")

driver = webdriver.ChromiumEdge(opts)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Click on shop to open the shopping page
driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
time.sleep(3)

# Select an element or Product form list of products
# Get the List of products
products_available = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products_available:
    product_name = product.find_element(By.XPATH,"div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH,'div/button').click()
        break

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()

# Enter the address
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("Ind")

# Wait for the dropdown to come
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

# Place order and validate
driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()
alert_text = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Success" in alert_text