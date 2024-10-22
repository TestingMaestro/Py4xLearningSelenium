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

    anchor_tag = driver.find_element(By.LINK_TEXT, "Start a free trial")
    anchor_tag.click()
    time.sleep(10)
    sso_page_title = driver.title
    print(sso_page_title)
    time.sleep(4)
    assert sso_page_title == "Get Started with Free Trial | VWO"
    driver.back()
