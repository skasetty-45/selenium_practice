from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

opts = Options()
opts.add_argument("headless")

driver = webdriver.ChromiumEdge()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

browser_provided_list =[]

# Sort the table in the web page
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# Take the Veggies in the Sorted order as we already clicked on the table header to sort
veggies_on_offer = driver.find_elements(By.XPATH,"//tr/td[1]")
for veggie in veggies_on_offer:
    browser_provided_list.append(veggie.text)

# The above code adds all the veggies to the list in sorted order
# Now we can sort them again to see that there is no change, before that we need to copy to the new list as the original list will be replaced if we perform sort operation
veggies_list_sorted_manual = browser_provided_list.copy()
browser_provided_list.sort()

assert veggies_list_sorted_manual == browser_provided_list