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


def test_vwo_error_check(browser_options):
    driver = webdriver.Chrome(browser_options)
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    user_email = driver.find_element(By.ID, "login-username")
    user_email.send_keys("abc@gmail.com")

    user_password = driver.find_element(By.NAME, "password")
    user_password.send_keys("pass123")

    sign_in_btn = driver.find_element(By.ID, "js-login-btn")
    sign_in_btn.click()
    time.sleep(5)

    error_message = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message.text)
    assert error_message.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
