# #!/usr/bin/env python
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import NoSuchElementException
import datetime
import logging

def log_timestamp():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (current_time + ' ')

# Start the browser and login with standard_user
def run_ui_tests(user, password):
    logging.INFO( log_timestamp() + 'Starting the browser...' )
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.nl/')

    # driver = webdriver.Chrome()
    logging.INFO(log_timestamp() + 'Browser started successfully.')
    logging.INFO(log_timestamp() + 'Navigating to the login page.')
    driver.get('https://www.saucedemo.com/')
    logging.INFO(log_timestamp() + 'Loging in to https://www.saucedemo.com/')
    driver.find_element_by_css_selector(
        'input[data-test="username"]').send_keys(user)
    driver.find_element_by_css_selector(
        'input[data-test="password"]').send_keys(password)
    driver.find_element_by_css_selector('input[value=Login]').click()

    logging.INFO(log_timestamp() + 'Searching for Products.')
    headerLabel = driver.find_element_by_class_name('header_secondary_container').text
    assert "PRODUCTS" in headerLabel
    logging.INFO(log_timestamp() + 'Successfully logged in ' + user + '.')
    logging.INFO(log_timestamp() + 'Selecting products.')
    products = driver.find_elements_by_css_selector('.inventory_item')
    logging.INFO(log_timestamp() + 'Adding products to cart.')
    for product in products:
        product_name = product.find_element_by_css_selector(
            '.inventory_item_name').text
        product.find_element_by_css_selector('button.btn_inventory').click()
        logging.INFO(log_timestamp() + product_name + ' successfully added to cart.')

    logging.INFO(log_timestamp() + 'Verifying if cart has been populated with 6 products.')
    cart_label = driver.find_element_by_css_selector(
        '.shopping_cart_badge').text
    assert cart_label == '6'

    logging.INFO(log_timestamp() + 'Navigating to shopping cart.')
    driver.find_element_by_css_selector('a.shopping_cart_link').click()
    assert '/cart.html' in driver.current_url, log_timestamp() + 'Navigation to shopping cart unsuccessful.'

    logging.INFO(log_timestamp() + 'Removing products from cart.')
    cart_products = driver.find_elements_by_css_selector('.cart_item')
    for product in cart_products:
        product_name = product.find_element_by_css_selector(
            '.inventory_item_name').text
        product.find_element_by_css_selector('button.cart_button').click()
        logging.INFO(log_timestamp() + product_name + ' successfully removed from cart.')
        
    logging.INFO(log_timestamp() + 'Confirming that shopping cart is empty.')
    if driver.find_elements_by_css_selector('.shopping_cart_badge'):
        cart_emptiness_flag = False
    else:
        cart_emptiness_flag = True
    
    assert cart_emptiness_flag == True
    logging.INFO(log_timestamp() + 'Shopping cart successfully emptied: ' + str(cart_emptiness_flag))

run_ui_tests('standard_user', 'secret_sauce')
