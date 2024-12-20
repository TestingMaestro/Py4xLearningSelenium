import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure


@allure.title("Verify alerts")
@allure.description("Handling Alerts")
def test_handling_alerts_accept(browser_options):
    driver = webdriver.Chrome(browser_options)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_ele = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    alert_ele.click()

    WebDriverWait(driver=driver, timeout=10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(6)
    alert.accept()

    result_text = driver.find_element(By.ID, "result")
    text_of = result_text.text

    assert text_of == "You clicked: Ok"


@allure.title("Verify alerts for dismiss")
@allure.description("Handling Alerts dismiss")
def test_handling_alerts_dismiss():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_ele = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']") # or
    alert_ele.click()

    WebDriverWait(driver=driver, timeout=20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(5)
    alert.send_keys("Yash")
    time.sleep(5)
    alert.accept()

    result_text = driver.find_element(By.ID, "result")
    text_of = result_text.text

    assert text_of == "You entered: Yash"

    time.sleep(5)
