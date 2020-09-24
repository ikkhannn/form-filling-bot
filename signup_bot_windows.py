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

def check_xpath(path,browser):
    try:
        element = browser.find_element_by_xpath(path)
        return element
    except NoSuchElementException:
        return None





def main():

    # df = pandas.read_csv('./products.csv')
    # products = df['products'].tolist()
    timeout = 10
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    params =  ["?utm_source=facebook&utm_medium=cpc&utm_campaign=100off","?utm_source=facebook&utm_medium=social&utm_campaign=100off","?utm_source=google&utm_medium=organic","?utm_source=facebook&utm_medium=cpc&utm_campaign=test_campaign"]
    browser = webdriver.Chrome(executable_path='C:/Users/me/Desktop/marketlytics/ecommerce bot/chromedriver.exe', chrome_options=option)
    base_url = "https://form-tracking.herokuapp.com/"

    try:
        # random_product = random.choice(products)
        random_params = random.choice(params)
        browser.get(base_url+random_params)
        print(base_url,random_params)
        time.sleep(2)
        # WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".single_add_to_cart_button"))).click()
        
        # WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'checkout-button'))).click()
        # time.sleep(2)

        WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, 'pwd')))        


        first_name = check_xpath('//*[@id="fname"]',browser)
        first_name.send_keys("first name")
        last_name = check_xpath('//*[@id="lname"]',browser)
        last_name.send_keys("last name")

        age = check_xpath('//*[@id="age"]',browser)
        age.send_keys("24")

        gender = Select(check_xpath('//*[@id="gender"]',browser))
        gender.select_by_visible_text('Female')
        address = check_xpath('//*[@id="address"]',browser)
        address.send_keys("my address")
        
        
        email = check_xpath('//*[@id="email"]',browser)
        email.send_keys("imran@marketlytics.com")
        notes = check_xpath('//*[@id="pwd"]',browser)
        notes.send_keys("Pa$$wOrd1!")
        
        time.sleep(10)
        browser.find_element_by_xpath('//*[@id="rememberMeCheckbox"]').click()

        WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.ID,"submit"))).click()
        

        print("Signed up!")
        time.sleep(5)
        browser.quit()
    except Exception as e:
        print(e)
        browser.quit()
        


if __name__ == '__main__':
    # service.py executed as script
        main()
    