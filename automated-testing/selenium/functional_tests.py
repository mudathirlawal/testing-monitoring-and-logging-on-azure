
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
    print ('Navigating to the demo page to login ...')
    driver.get('https://www.saucedemo.com/')

def add_product_to_cart( driver ):
    product = driver.find_element_by_class_name('inventory_item')
    add_to_cart_button = driver.find_element_by_xpath(
        "//div[@class='btn_inventory']").click()
    
# Make `driver` variable global:
driver = set_up_driver()

# Login as `standard_user`:
login('standard_user', 'secret_sauce')
