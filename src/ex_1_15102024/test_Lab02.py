from selenium import webdriver
import pytest


def test_app_vwo_login():
    # POST Request which create a session for a Chrom()-->session id
    driver = webdriver.Chrome()

    driver.get("https://app.vwo.com")  # Post request
    print(driver.title)  # GET request
    assert driver.title == "Login - VWO"
