# This program will use the default payment method and address, so please ensure they are correct
from selenium import webdriver as wd
#import pyautogui
import random
import time

email = "Enter Email here"
password = "Enter Password Here"
amazon_url_rtx_3090 = "https://www.amazon.ca/Gaming-GeForce-Extreme-384BIT-ZT-A30900B-10P/dp/B09GS7Q8P5/ref=sr_1_2?crid=3EQX430A2KJKS&keywords=rtx+3090&qid=1640778110&sprefix=rtx+3090%2Caps%2C261&sr=8-2"
driver = wd.Chrome("chromedriver.exe")

is_ordered = False

while not is_ordered:

    wait_time = random.randrange(7.0, 20.0)
    print(wait_time)
    time.sleep(wait_time)

    driver.get(amazon_url_rtx_3090)

    if not driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').size() == 0:
        add_to_cart_button = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
        add_to_cart_button.click()

        sign_in_button = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]')
        sign_in_button.click()

        email_textbox = driver.find_element_by_id('ap_email')
        email_textbox.send_keys(email)
        #pyautogui.press('enter')

        password_textbox = driver.find_element_by_id('ap_password')
        password_textbox.send_keys(password)
        #pyautogui.press('enter')

        not_now_button = driver.find_element_by_id('ap-account-fixup-phone-skip-link')
        not_now_button.click()

        go_to_checkout_button = driver.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]/span/input')
        go_to_checkout_button.click()

        ship_to_address_button = driver.find_element_by_xpath('//*[@id="orderSummaryPrimaryActionBtn"]/span/input')
        ship_to_address_button.click()

        use_payment_method_button = driver.find_element_by_xpath('//*[@id="orderSummaryPrimaryActionBtn"]/span/input')
        use_payment_method_button.click()

        place_order_button = driver.find_element_by_xpath('//*[@id="bottomSubmitOrderButtonId"]/span/input')
        place_order_button.click()

        is_ordered = True
