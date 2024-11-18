from selenium import webdriver
from selenium.webdriver.edge.options import Options

opts = Options()
opts.add_argument("headless")

driver = webdriver.ChromiumEdge(opts)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Lets scroll the page
driver.execute_script("window.scrollBy(0,500);")
driver.save_screenshot("test_result.png")
