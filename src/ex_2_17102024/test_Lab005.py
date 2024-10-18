import time
import allure
from selenium import webdriver
import pytest


@allure.title("Current Url verification in chrome")
@allure.description("Verify the headless mode")
def test_current_url_verification_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    current_url = driver.current_url
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"


@allure.title("Current Url verification in edge")
@allure.description("Verify the headless mode")
def test_current_url_verification_edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    current_url = driver.current_url
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"
