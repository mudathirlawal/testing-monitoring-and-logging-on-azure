# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import NoSuchElementException
import datetime
import sys
# import logging

def log_timestamp():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (current_time + '\t')

# Start the browser and login with standard_user
def login(user, password):
    print( log_timestamp() + 'Starting the browser...' )
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.nl/')

    # driver = webdriver.Chrome()
    print(log_timestamp() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    print(log_timestamp() + 'Loging in to https://www.saucedemo.com/')
    driver.find_element_by_css_selector(
        'input[data-test="username"]').send_keys(user)
    driver.find_element_by_css_selector(
        'input[data-test="password"]').send_keys(password)
    driver.find_element_by_css_selector('input[value=Login]').click()

    print(log_timestamp() + 'Searching for Products')
    headerLabel = driver.find_element_by_class_name('header_secondary_container').text
    assert "PRODUCTS" in headerLabel
    print(log_timestamp() + 'Successfully logged in, user: ' + user)

    print(log_timestamp() + 'Find products')
    products = driver.find_elements_by_css_selector('.inventory_item')

    print(log_timestamp() + 'Add products to cart')
    for product in products:
        product_name = product.find_element_by_css_selector(
            '.inventory_item_name').text
        product.find_element_by_css_selector('button.btn_inventory').click()
        print(log_timestamp() + 'Product added to cart: ' + product_name)

    print(log_timestamp() + 'Verify if cart has 6 added products')
    cart_label = driver.find_element_by_css_selector(
        '.shopping_cart_badge').text
    assert cart_label == '6'

    print(log_timestamp() + 'Navigate to cart')
    driver.find_element_by_css_selector('a.shopping_cart_link').click()
    assert '/cart.html' in driver.current_url, log_timestamp() + 'Cart navigation unsuccessful'

    print(log_timestamp() + 'Removing products from cart')
    cart_products = driver.find_elements_by_css_selector('.cart_item')
    for product in cart_products:
        product_name = product.find_element_by_css_selector(
            '.inventory_item_name').text
        product.find_element_by_css_selector('button.cart_button').click()
        print(log_timestamp() + 'Removed from cart: ' + product_name)

    print(log_timestamp() + 'Confirm that shopping cart is empty')

    if driver.find_elements_by_css_selector('.shopping_cart_badge'):
        print(log_timestamp() + 'Shopping cart is empty')
        cart_emptiness_flag = False
    else:
        cart_emptiness_flag = True

    assert cart_emptiness_flag == True
    print(log_timestamp() + 'All items have been emptied from cart: ' + cart_emptiness_flag)

login('standard_user', 'secret_sauce')
