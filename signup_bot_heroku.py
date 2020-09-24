# This script gets the hrefs of all products on the website.
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import csv
import os
import pandas
import random
import time

#variables

times_to_run = 5
interval = 120

def check_xpath(path,browser):
    try:
        element = browser.find_element_by_xpath(path)
        return element
    except NoSuchElementException:
        return None



def main():

    df = pandas.read_csv('./products.csv')
    products = df['products'].tolist()
    timeout = 10
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    option.add_argument('--headless')
    option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')
    option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--no-sandbox')
    params =  ["?utm_source=facebook&utm_medium=cpc&utm_campaign=100off","?utm_source=facebook&utm_medium=social&utm_campaign=100off","?utm_source=google&utm_medium=organic","?utm_source=facebook&utm_medium=cpc&utm_campaign=test_campaign"]
    browser = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=option)


    try:
        random_product = random.choice(products)
        random_params = random.choice(params)
        browser.get(random_product+random_params)
        print(random_product,random_params)
        time.sleep(2)
        WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".single_add_to_cart_button"))).click()
        
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'checkout-button'))).click()
        time.sleep(2)

        first_name = check_xpath('//*[@id="billing_first_name"]',browser)
        first_name.send_keys("first name")
        last_name = check_xpath('//*[@id="billing_last_name"]',browser)
        last_name.send_keys("last name")

        company_name = check_xpath('//*[@id="billing_company"]',browser)
        company_name.send_keys("company")

        country = Select(check_xpath('//*[@id="billing_country"]',browser))
        country.select_by_visible_text('Pakistan')
        street_address_1 = check_xpath('//*[@id="billing_address_1"]',browser)
        street_address_1.send_keys("my address")
        street_address_2 = check_xpath('//*[@id="billing_address_2"]',browser)
        street_address_2.send_keys("my address")
        
        city = check_xpath('//*[@id="billing_city"]',browser)
        city.send_keys("karachi")
        
        state = Select(check_xpath('//*[@id="billing_state"]',browser))
        state.select_by_visible_text('Sindh')
        zipcode = check_xpath('//*[@id="billing_postcode"]',browser)
        zipcode.send_keys("222222")
        
        phone = check_xpath('//*[@id="billing_phone"]',browser)
        phone.send_keys("1234567")
        
        email = check_xpath('//*[@id="billing_email"]',browser)
        email.send_keys("imran@marketlytics.com")
        notes = check_xpath('//*[@id="order_comments"]',browser)
        notes.send_keys("my notes")
        

        WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.ID,"payment_method_cheque"))).click()

        time.sleep(10)
        WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.ID,"place_order"))).click()
        
        print("Order completed")
        time.sleep(10)
        browser.quit()

    except Exception as e:
        print(e)
        browser.quit()

if __name__ == '__main__':
    # service.py executed as script
    for i in range(times_to_run):
        main()
        if(i<times_to_run-1):
            time.sleep(interval)
