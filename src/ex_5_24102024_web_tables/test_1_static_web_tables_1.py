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
def test_web_tables_1(driver):
    driver.get("https://awesomeqa.com/webtable.html")
    time.sleep(10)

    row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    row = len(row_elements)
    col = len(col_elements)

    # fp = "//table[@id='movies']/tbody/tr["
    # sp = "]/td["
    # tp = "]"

    first_part = "//table[@id='customers']/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            dynamic_path_text = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in dynamic_path_text:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_path_txt = driver.find_element(By.XPATH, country_path).text
                print(country_path_txt)
