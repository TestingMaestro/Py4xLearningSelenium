# app.vwo.com
# url
# find the email
# find the password
# find the login button and click on login
# fin the email text
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwo_start_free_trial(browser_options):
    driver = webdriver.Chrome(browser_options)
    driver.get("https://app.vwo.com/#/login")

    no_of_buttons = driver.find_elements(By.TAG_NAME, "button")
    print(len(no_of_buttons))  # to print number of buttons in VWO Login page
    time.sleep(8)
    for buttons_text in no_of_buttons:
        print(buttons_text.text)  # print all buttons text in the VWO Login page
