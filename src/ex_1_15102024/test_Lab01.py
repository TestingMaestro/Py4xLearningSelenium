from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
import pytest


# selenium 3 ->
# def test_launch_chrome_selenium3():
#     driver_path = 'C:/Python-Selenium/chromedriver/chromedriver-win64/chromedriver.exe'
#     service = Service(executable_path=driver_path)
#     driver = webdriver.Chrome(service=service)
#     driver.get("https://app.vwo.com")

#in selenium 4
def test_launch_chrome():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    current_url = driver.current_url
    assert current_url == "https://app.vwo.com/#/login"
