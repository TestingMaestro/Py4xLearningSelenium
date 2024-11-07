import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Action P1 - ActionChains class")
@allure.description("Verify the Actions P1")
def test_actions_p1():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")

    actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "please enter the first name")
    actions.key_up(Keys.SHIFT).perform()

    time.sleep(10)
