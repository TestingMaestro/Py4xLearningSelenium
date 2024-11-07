# Alerts
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure


@allure.title("Verify alerts for accept")
@allure.description("Handling Alerts accept")
def test_alerts_conf_prompt(browser_options):
    driver = webdriver.Chrome(browser_options)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    alert_ele = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    alert_ele = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    alert_ele = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
    alert_ele.click()

    WebDriverWait(driver=driver, timeout=10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(6)
    # Alert
    alert.accept()

    # confirmation

    alert.accept()
    alert.dismiss()

    # prompt
    alert.send_keys("Test alert")
    alert.accept()
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result")
    text_of = result_text.text

    assert text_of == "You clicked: Ok"
