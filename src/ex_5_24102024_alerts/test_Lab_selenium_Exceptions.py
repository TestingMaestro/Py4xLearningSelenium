import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Verify SVG")
@allure.description("Handling SVG")
def test_handling_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    try:
        driver.find_element("by.e]")
    except Exception as e:
        print(e)
