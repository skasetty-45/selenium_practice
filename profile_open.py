import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
# Uncomment this line if you want to run the browser headless
# opts.add_argument("headless")

# Add the profile directory if you want to use your existing Edge profile
opts.add_argument("--profile-directory=/Users/saratkasetty/Library/Application Support/Microsoft Edge/")
opts.add_argument("profile-directory=Default")

# Path to Edge WebDriver; make sure it's correctly set in your PATH
driver = webdriver.ChromiumEdge(options=opts)

try:
    driver.get("https://www.bing.com/search?q=hekkington")

finally:
    driver.quit()  # Ensure the browser closes after the script finishes
