import time
import allure
from selenium import webdriver
import pytest


@allure.title("Verify the headless mode")
@allure.description("Verify the headless mode")
def test_chrome_options():
    options = webdriver.ChromeOptions()
    # command line arguments before running browser --> chrome
    options.add_argument("--incognito")  # runs chrome in incognito mode
    options.add_argument("--start-maximized")  # Start window maximized
    options.add_argument("--window-size=900,600")  # window size customization
    options.add_argument("--disable-infobars")
    # in Chrome disables the "Chrome is being controlled by automated software notification bar during Selenium tests
    options.add_argument("--headless")  # runs chrome in headless mode - NO UI-- better performance
    driver = webdriver.Chrome(options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    current_url = driver.current_url
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"
