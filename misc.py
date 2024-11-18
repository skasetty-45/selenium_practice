from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Lets scroll the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.save_screenshot("test_result.png")