import time
import allure
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@allure.title("Current Url verification in chrome")
@allure.description("Verify the headless mode")
def test_current_url_verification_chrome(headless_mode):
    driver = webdriver.Chrome(headless_mode)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    current_url = driver.current_url
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"


@allure.title("Current Url verification in edge")
@allure.description("Verify the headless mode")
def test_current_url_verification_edge(headless_mode):
    driver = webdriver.Edge(headless_mode)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    current_url = driver.current_url
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"


@allure.title("Current Url verification in Firefox")
@allure.description("Verify the headless mode")
def test_current_url_verification_firefox(headless_mode):
    driver = webdriver.Firefox(headless_mode)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    current_url = driver.current_url
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"
