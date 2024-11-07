import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@allure.title("Verify 1 end to end flow for myntra website")
@allure.description("Verify end-t0-end flow")
def test_myntra_website(driver):
    driver.get("https://www.myntra.com/")
    element = driver.find_element(By.XPATH, "//a[@data-group='men']/parent::div/a")
    actions = ActionChains(driver)
    WebDriverWait(driver=driver, timeout=6).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@data-group='men']/parent::div/a")))
    actions.move_to_element(element).perform()
    time.sleep(6)
