# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging

# Start the browser and login with standard_user
def functional_ui_test(user, password):
    logging.basicConfig(filename='selenium.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    logging.info('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 

    driver = webdriver.Chrome(options=options)
    
    # for debugging enable driver constructor with no options
    # driver = webdriver.Chrome()

    # Test Login to the site
    logging.info('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_css_selector("input[id='login-button']").click()

    path_content_div = "div[id='page_wrapper'] > div[id='contents_wrapper'] > div[id='inventory_container'] > div"
    results = driver.find_element_by_css_selector(path_content_div + " > div[class='header_secondary_container'] > div[id='inventory_filter_container'] > div[class='product_label']").text
    assert "Products" in results
    logging.info("Successfully logged in as " + user)


    # Test Add Items to Shopping Cart
    logging.info("Starting the shopping...")
    path_inventory_item = path_content_div + " > div[id='inventory_container'] > div[class='inventory_list'] > div[class='inventory_item']"
    product_items = driver.find_elements_by_css_selector(path_inventory_item)
    assert len(product_items) == 6
    logging.info("Successfully found 6 product items.")    
    
    for i in range(6):
        path_product_item_name = path_inventory_item + " > div[class='inventory_item_label'] > a[id='item_" + str(i) + "_title_link'] > div[class='inventory_item_name']"
        product_item_name = driver.find_element_by_css_selector(path_product_item_name)
        product_item_name.find_element_by_xpath('..//..//..//div[@class="pricebar"]//button[@class="btn_primary btn_inventory"]').click()
        logging.info("Succesfully added to shopping cart: " + product_item_name.text)

    path_shopping_cart_link = "div[id='page_wrapper'] > div[id='contents_wrapper'] > div[id='header_container'] > div[id='shopping_cart_container'] > a.shopping_cart_link.fa-layers.fa-fw"
    path_shopping_cart_badge = path_shopping_cart_link + " > span.fa-layers-counter.shopping_cart_badge"
    shopping_cart_total_items = driver.find_element_by_css_selector(path_shopping_cart_badge).text
    assert '6' == shopping_cart_total_items
    logging.info("Succesfully added to shopping cart: 6 items in total")


    # Test Remove Items from Shopping Cart
    logging.info("A spouse came in, need to destroy the the evidence... ;-)")
    driver.find_element_by_css_selector(path_shopping_cart_link).click()
    path_cart_title = "div[id='page_wrapper'] > div[id='contents_wrapper'] > div[class='subheader']"
    cart_title = driver.find_element_by_css_selector(path_cart_title).text
    assert 'Your Cart' in cart_title
    logging.info("Successfully entered the shopping cart page.")

    path_cart_item_remove_buttons = "div[id='page_wrapper'] > div[id='contents_wrapper'] > div[id='cart_contents_container'] > div > div[class='cart_list'] > div[class='cart_item'] > div[class='cart_item_label'] > div[class='item_pricebar'] > button[class='btn_secondary cart_button']"
    remove_item_buttons = driver.find_elements_by_css_selector(path_cart_item_remove_buttons)
    
    for remove_button in remove_item_buttons:
        shopping_cart_item_name = remove_button.find_element_by_xpath('..//..//a[contains(@id, "_title_link")]//div[@class="inventory_item_name"]').text
        remove_button.click()
        logging.info("Succesfully removed an item from shopping cart: " + shopping_cart_item_name)

    shopping_cart_total_items = driver.find_elements_by_css_selector(path_shopping_cart_badge)
    assert 0 == len(shopping_cart_total_items)
    logging.info("Succesfully removed all items from shopping cart.")


functional_ui_test('standard_user', 'secret_sauce')