
#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser:
def set_up_driver():
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print ('Browser started successfully!')
    return driver

# Make `driver` variable global:
driver = set_up_driver()

# Define login:
def login( user, password, driver ):
    print ('Navigating to the demo page to login ...')
    driver.get('https://www.saucedemo.com/')

# Login as `standard_user`:
login('standard_user', 'secret_sauce')

def add_all_products_to_cart( driver ):
    products = driver.find_element_by_class_name('inventory_item')
    add_to_cart_button = driver.find_element_by_xpath(
        "//input[@name='continue'][@type='button']")

# driver.find_element_by_xpath(
#     "//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input']"
#     ).click()
# driver.find_element_by_xpath(
#     "//span[contains(text(), 'Samsung 80 cm (32 Inches) Series 4 Ready LED TV']"
#     ).click()


