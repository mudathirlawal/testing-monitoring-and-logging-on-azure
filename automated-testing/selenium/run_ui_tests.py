
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

# Define login:
def login( user, password, driver ):
    uri = 'https://www.saucedemo.com/'
    print ('Navigating to the demo page to login ...')
    driver.get( uri )

# Add product to cart:
def add_product_to_cart( driver ):
    product = driver.find_element_by_class_name('inventory_item')
    add_to_cart_button = driver.find_element_by_css_selector(
    "button.btn_secondary.btn_inventory")
    add_to_cart_button.click()

def remove_product_from_cart( driver ):
    product = driver.find_element_by_class_name('inventory_item')
    add_to_cart_button = driver.find_element_by_css_selector(
    "button.btn_secondary.btn_inventory")
    add_to_cart_button.click()

# Make `driver` variable global:
driver = set_up_driver()

# Login as `standard_user`:
login('standard_user', 'secret_sauce')
