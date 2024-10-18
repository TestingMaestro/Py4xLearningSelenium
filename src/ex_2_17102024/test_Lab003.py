from selenium import webdriver

import allure, pytest


def test_vwo_login():
    driver = webdriver.Chrome()
    page_source = driver.page_source
    print(page_source)

