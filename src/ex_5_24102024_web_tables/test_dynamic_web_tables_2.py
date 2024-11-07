import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Verify 1 end to end flow for myntra website")
@allure.description("Verify end-t0-end flow")
def test_web_tables_static_1():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")

    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for rows in row_table:
        cols = rows.find_elements(By.TAG_NAME, "td")
        for e in cols:
            print(e.text)

    time.sleep(5)
