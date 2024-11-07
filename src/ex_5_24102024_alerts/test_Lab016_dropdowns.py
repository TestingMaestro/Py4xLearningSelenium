import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Verify Dropdowns")
@allure.description("Handling Dropdowns")
def test_handling_dropdowns_single():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_ele = driver.find_element(By.CSS_SELECTOR, "select#dropdown")
    select = Select(dropdown_ele)
    select.select_by_index(1)
    select.select_by_value("Option 1")
    time.sleep(5)


def test_handling_dropdowns_multiple():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/91914/Desktop/Multiselect%20ropdowns.html")

    dropdown_ele = driver.find_element(By.ID, "cars")
    select = Select(dropdown_ele)
    for eles in range(len(select.options)):
        select.select_by_index(eles)
        time.sleep(5)
