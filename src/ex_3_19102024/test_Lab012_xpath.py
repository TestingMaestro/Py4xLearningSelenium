# by XPath
import os
import time

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


def test_vwo_using_xpath(browser_options, launch_chrome):
    load_dotenv()
    user_name = launch_chrome.find_element(By.XPATH, "//input[@id='login-username']")
    user_name.send_keys(os.getenv("USERNAME"))
    password = launch_chrome.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys(os.getenv("PASSWORD"))
    time.sleep(4)
